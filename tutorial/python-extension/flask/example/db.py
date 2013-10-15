import datetime
from hashlib import md5
import json

from peewee import *
import settings

# create a peewee database instance -- our models will use this database to
# persist information
app_database = SqliteDatabase(settings.DATABASE)

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage. for more information, see:
# http://charlesleifer.com/docs/peewee/peewee/models.html#model-api-smells-like-django
class BaseModel(Model):
    	class Meta:
        	database = app_database

# the user model specifies its fields (or columns) declaratively, like django
class User(BaseModel):
    	username = CharField()
    	password = CharField()
    	email = CharField()
    	join_date = DateTimeField()

    	class Meta:
        	order_by = ('username',)

   	 # it often makes sense to put convenience methods on model instances, for
    	# example, "give me all the users this user is following":
    	def following(self):
        	# query other users through the "relationship" table
        	return User.select().join(
            	Relationship, on=Relationship.to_user,
        	).where(Relationship.from_user == self)

    	def followers(self):
	        return User.select().join(
	            Relationship, on=Relationship.from_user,
	        ).where(Relationship.to_user == self)
	
    	def is_following(self, user):
	        return Relationship.select().where(
	            (Relationship.from_user == self) &
	            (Relationship.to_user == user)
	        ).count() > 0
	
    	def gravatar_url(self, size=80):
	        url =  'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
	            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)
		return url

# this model contains two foreign keys to user -- it essentially allows us to
# model a "many-to-many" relationship between users.  by querying and joining
# on different columns we can expose who a user is "related to" and who is
# "related to" a given user
class Relationship(BaseModel):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')


# a dead simple one-to-many relationship: one user has 0..n messages, exposed by
# the foreign key.  because we didn't specify, a users messages will be accessible
# as a special attribute, User.message_set
class Message(BaseModel):
    user = ForeignKeyField(User)
    content = TextField()
    pub_date = DateTimeField()

    class Meta:
        order_by = ('-pub_date',)


# simple utility function to create tables
def create_tables():
	app_database.connect()
	# true: fail silently if table exists
    	User.create_table(True)
    	Relationship.create_table(True)
    	Message.create_table(True)
	app_database.close()

def create_records():
        user = User.create(
                username='kezunlin',
                password=md5('123456').hexdigest(),
                email='zunlin1234@gmail.com',
                join_date=datetime.datetime.now())
        message = Message.create(
            user=user,
            content='Hello world. This is the first message.',
            pub_date=datetime.datetime.now())

def create_records_for():
	user = User.get(User.username=='kezunlin')
	for i in range(15):
        	message = Message.create(
            		user=user,
            		content='Message #{0}'.format(i+1),
            		pub_date=datetime.datetime.now())

def create_user_following():
	ke = User.get(User.username=='kezunlin')
	for i in range(3):
        	user = User.create(
                	username='kezunlin{0}'.format(i+2),
                	password=md5('123456').hexdigest(),
                	email='zunlin1234@gmail.com',
                	join_date=datetime.datetime.now())
		for i in range(5):
        		message = Message.create(
            			user=user,
            			content='User {0} Message #{1}'.format(user.username,i+1),
            			pub_date=datetime.datetime.now())
		Relationship.create(from_user=ke,to_user=user)
		Relationship.create(from_user=user,to_user=ke)

def main():
	#create_tables()
	#create_records()
	#create_records_for()
	#create_user_following()
	pass

if __name__=="__main__":
	main()

