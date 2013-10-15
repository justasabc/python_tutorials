"""
bugs:
1) session['user'] = user ,user can not be serialized as json(because of DateTimeField)
2) @app.template_filter does not work. In template, use variable instead
"""
import datetime

from flask import Flask
from flask import request,session,g
from flask import url_for, redirect, abort, render_template, flash
from functools import wraps
from hashlib import md5
from db import Message,User,Relationship,app_database
import settings

# create a flask application - this ``app`` object will be used to handle
# inbound requests, routing them to the proper 'view' functions, etc
app = Flask(__name__)
# read configurations from config file
app.config.from_pyfile('settings.py',silent=False) # read config(all UPPERCASE variables) from __name__ module

# flask provides a "session" object, which allows us to store information across
# requests (stored by default in a secure cookie).  this function allows us to
# mark a user as being logged-in by setting some values in the session data:
def auth_user(user):
    	session['logged_in'] = True
    	#session['user'] = user # ERROR: DateTimeField can not be serialized
    	session['username'] = user.username
    	flash('You are logged in as %s' % (user.username))

def get_session_user():
	username = session.get('username',None)
	if username:
		user = User.get(User.username==username)
		return user
	return None

# view decorator which indicates that the requesting user must be authenticated
# before they can access the view.  it checks the session to see if they're
# logged in, and if not redirects them to the login view.
def login_required(f):
    	@wraps(f)
    	def inner(*args, **kwargs):
        	if not session.get('logged_in'):
            		return redirect(url_for('login'))
        	return f(*args, **kwargs)
    	return inner

# given a template and a SelectQuery instance, render a paginated list of
# objects from the query inside the template
#def object_list(template_name, qr, var_name='object_list', **kwargs):
def object_list(template_name, qr, var_name, **kwargs):
    	kwargs.update(
		# http://localhost:5000/?page=2
        	page=int(request.args.get('page', 1)), # page is 1-based
        	pages=qr.count() / settings.PER_PAGE + 1
    	)
    	kwargs[var_name] = qr.paginate(kwargs['page'],settings.PER_PAGE)
    	return render_template(template_name, **kwargs)

# retrieve a single object matching the specified query or 404 -- this uses the
# shortcut "get" method on model, which retrieves a single object or raises a
# DoesNotExist exception if no matching object exists
# http://charlesleifer.com/docs/peewee/peewee/models.html#Model.get)
def get_object_or_404(model, **kwargs):
    	try:
        	return model.get(**kwargs)
    	except model.DoesNotExist:
        	abort(404)

# custom template filter -- flask allows you to define these functions and then
# they are accessible in the template -- this one returns a boolean whether the
# given user is following another user.
@app.template_filter('is_following')
def is_following(from_user,to_user):
	return from_user.is_following(to_user)

# request handlers -- these two hooks are provided by flask and we will use them
# to create and tear down a database connection on each request.  peewee will do
# this for us, but its generally a good idea to be explicit.
@app.before_request
def before_request():
    	g.db = app_database
    	g.db.connect()

@app.after_request
def after_request(response):
    	g.db.close()
    	return response

# views -- these are the actual mappings of url to view function
@app.route('/')
def homepage():
    # depending on whether the requesting user is logged in or not, show them
    # either the public timeline or their own private timeline
    	if session.get('logged_in'):
        	return private_timeline()
    	else:
        	return public_timeline()

@app.route('/public/')
def public_timeline():
    	# simply display all messages, newest first
    	messages = Message.select()
    	return object_list('public_messages.html', messages, 'message_list')

@app.route('/private/')
@login_required
def private_timeline():
    	# the private timeline exemplifies the use of a subquery -- we are asking for
    	# messages where the person who created the message is someone the current
    	# user is following.  these messages are then ordered newest-first.
    	user = get_session_user()
	assert user is not None
    	messages = Message.select().where(
        	Message.user << user.following()
    	)
    	return object_list('private_messages.html', messages, 'message_list')

@app.route('/my/')
@login_required
def my_timeline():
    	user = get_session_user()
	assert user is not None
    	messages = Message.select().where(
        	Message.user == user
    	)
    	return object_list('my_messages.html', messages, 'message_list')

@app.route('/join/', methods=['GET', 'POST'])
def join():
	if request.method == 'GET':
		return render_template('join.html')
	username = request.form.get('username')
	password = request.form.get('password')
	email = request.form.get('email')
	if not username:
		flash('Please input username')
            	return redirect(url_for('join'))
	elif not password:
		flash('Please input password')
            	return redirect(url_for('join'))
	elif not email:
		flash('Please input email')
            	return redirect(url_for('join'))
        try:
         	# use the .get() method to quickly see if a user with that name exists
           	user = User.get(username=username)
            	flash('That username is already taken')
	except User.DoesNotExist:
           	# if not, create the user and store the form data on the new model
            	user = User.create(username=username,
			password=md5(password).hexdigest(),	
			email=email,join_date=datetime.datetime.now())
            		# mark the user as being 'authenticated' by setting the session vars
           	auth_user(user)
            	return redirect(url_for('homepage'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	username = request.form.get('username')
	password = request.form.get('password')
	if not username:
		flash('Please input username')
            	return redirect(url_for('login'))
	elif not password:
		flash('Please input password')
            	return redirect(url_for('login'))
        try:
            user = User.get(
                username=username,
                password=md5(password).hexdigest()
            )
        except User.DoesNotExist:
		flash('The username or password is incorrect')
            	return redirect(url_for('login'))
        else:
		auth_user(user)
        	return redirect(url_for('homepage'))

@app.route('/logout/')
@login_required
def logout():
	session.pop('logged_in',None)
	session.pop('username', None)
	flash('You were logged out')
    	return redirect(url_for('homepage'))

@app.route('/following/')
@login_required
def following():
    	user = get_session_user()
	assert user is not None
    	return object_list('user_following.html', user.following(), 'user_list')

@app.route('/followers/')
@login_required
def followers():
    	user = get_session_user()
	assert user is not None
    	return object_list('user_followers.html', user.followers(), 'user_list')

@app.route('/users/')
def user_list():
    	users = User.select()
    	return object_list('user_list.html', users, 'user_list')

@app.route('/users/<username>/')
def user_detail(username):
    	# using the "get_object_or_404" shortcut here to get a user with a valid
    	# username or short-circuit and display a 404 if no user exists in the db
    	user = get_object_or_404(User, username=username)

    	# get all the users messages ordered newest-first -- note how we're accessing
    	# the messages -- user.message_set.  could also have written it as:
    	# Message.select().where(user=user).order_by(('pub_date', 'desc'))
    	messages = user.message_set
	session_user = get_session_user()

	if session_user:
		is_login = True
		isfollowing = is_following(session_user,user)
	else:
		is_login = False
		isfollowing = False
    	return object_list('user_detail.html', messages, 'message_list', user=user,is_following=isfollowing, is_login=is_login)

@app.route('/users/<username>/follow/', methods=['POST'])
@login_required
def user_follow(username):
    	user = get_object_or_404(User, username=username)
    	Relationship.get_or_create(
        	from_user=get_session_user(),
        	to_user=user,
    	)
    	flash('You are now following %s' % user.username)
    	return redirect(url_for('user_detail', username=user.username))

@app.route('/users/<username>/unfollow/', methods=['POST'])
@login_required
def user_unfollow(username):
    	user = get_object_or_404(User, username=username)
    	Relationship.delete().where(
        	(Relationship.from_user == get_session_user()) &
        	(Relationship.to_user == user)
    	).execute()
    	flash('You are no longer following %s' % user.username)
    	return redirect(url_for('user_detail', username=user.username))

@app.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    	if request.method == 'GET':
		return render_template('create.html')
	content = request.form.get('content')
	if not content:
        	flash('Please input message')
		return redirect(url_for('create'))
    	user = get_session_user()
	assert user is not None
        message = Message.create(
           user=user,
           content=content,
           pub_date=datetime.datetime.now()
        )
        flash('Your message has been created')
        return redirect(url_for('user_detail', username=user.username))

# allow running from the command line
if __name__ == '__main__':
    	app.run(host=settings.HOST,port=settings.PORT,debug=settings.DEBUG)
