from flask import Flask,url_for,render_template,redirect,abort,make_response,request,session,g,flash
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route("/")
def index():
    	return "Hello World!"

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
	return render_template('hello.html',name=name)

@app.route("/user/<username>")
def show_user_profile(username):
	return "User %s" % username

# int  float path

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "Post %d" % post_id
"""
In the first case, the canonical URL for the projects endpoint has a trailing slash. In that sense, it is similar to a folder on a file system. Accessing it without a trailing slash will cause Flask to redirect to the canonical URL with the trailing slash.
"""
@app.route("/projects/")
def projects():
	# localhost:5000/projects ----> localhost:5000/projects/  (URL Redirect)
	# localhost:5000/projects/ ---->  OK
	return "THe projects page!"

"""
In the second case, however, the URL is defined without a trailing slash, rather like the pathname of a file on UNIX-like systems. Accessing the URL with a trailing slash will produce a 404 Not Found error.
"""
@app.route("/about")
def about():
	# localhost:5000/about ---->  OK
	# localhost:5000/about/ ---->  404 ERROR: URL NOT FOUND
	# The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
	return "THe about page!"

def test_url_for():
	with app.test_request_context():
		# url_for:  function name  **kwargs
		print url_for('index')
		print url_for('hello')
		print url_for('show_user_profile',username='kezunlin')
		print url_for('show_post',post_id=12)
		print url_for('projects')
		print url_for('about')

def test_static():
	with app.test_request_context():
		print url_for('static',filename='1.txt')

def test_request():
	with app.test_request_context('/xxx',method='POST'):
		assert request.path == '/xxx'
		assert request.method == 'POST'
		print request

@app.route('/query')
def query():
	# request is a global object
	# GET:  request.args
	# POST: request.form  request.files
	if request.method == 'GET':
		# http://localhost:5000/query?username=xxx&password=yyy
		username = request.args.get('username','default')
		password = request.args.get('password','******')
		return "Query: {0}-{1}".format(username,password)

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username',None)
		password = request.form.get('password',None)
		#username = request.form['username']
		#password = request.form['password']
		if username and password:
			return "POST: Login successfully for {0}---{1}".format(username,password)
		else:
			return "Please fill username and password"
	else:
		return render_template('login.html')

# upload a file
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploaded/<filename>')
def uploaded_file(filename=None):
	if filename:
		return "Uploaded {0} successfully.".format(filename)
	else:
		return "Please input a filename"

@app.route('/error/<msg>')
def error(msg=None):
	if msg:
		return "ERROR:  {0}".format(msg)
	else:
		return "Please input a msg"

@app.route('/upload',methods=['GET','POST'])
def upload_file():
    	if request.method == 'POST':
        	f = request.files.get('upload_filename',None)
        	if f and allowed_file(f.filename):
            		sfilename = secure_filename(f.filename)
            		f.save(os.path.join(UPLOAD_FOLDER,sfilename))
            		re_url= url_for('uploaded_file', filename=sfilename)
            		return redirect(re_url)
		else:
			error = "file is not allowed."
            		re_url= url_for('error', msg=error)
            		return redirect(re_url)
    	return render_template('upload.html')

@app.route('/cookie')
def cookie():
	username = request.cookies.get('username')	
	if username:
		return "Username is {0}".format(username)
	else:
		resp = make_response(render_template('login.html'))
		resp.set_cookie('username','xxxyyyzzz')
		return resp

@app.route('/redirect')
def myredirect():
	return redirect(url_for('login'))

@app.route('/abort')
def myabort():
	abort(401)
	print "This is never executed!"

# set session secret key
app.secret_key = os.urandom(24)
@app.route('/mysession')
def mysession():
	# check whether username is in session
	if 'username' in session:
		return "Logged in as {0}".format(session['username'])
	return 'You are not logged in'

@app.route("/slogin",methods=['GET','POST'])
def slogin():
	if request.method == 'POST':
		username = request.form.get('username',None)
		password = request.form.get('password',None)
		if username and password:
			# add username to session
			session['username'] = username
			reurl = url_for('mysession')
			print reurl
			return redirect(reurl)
	else:
		return render_template('slogin.html')

@app.route('/slogout')
def slogout():
	# remove username from session if it's there
	session.pop('username',None)
	reurl = url_for('mysession')
	print reurl
	return redirect(reurl)

# app.logger
@app.route('/logger')
def mylogger():
	app.logger.debug('A value for debugging')
	app.logger.warning('A warning occurred (%d apples)', 42)
	app.logger.error('An error occurred')
	return 'Logging information to console'

# message flashing
@app.route('/flash')
def myflash():
	flash('You were successfully logged in')
	return render_template('flash.html')

if __name__ == "__main__":
	test_url_for()
	test_static()
	test_request()
	#app.run(debug=True,host='0.0.0.0')
	app.run(debug=True)
