from peewee import *
from datetime import date

db = SqliteDatabase('people.db')


class BaseModel(Model):
	class Meta:
		database = db

class Person(BaseModel):
	name = CharField()
	birthday = DateField()
	is_relative = BooleanField()

	def __str__(self):
		return "{0} {1} {2}".format(self.name,self.birthday,self.is_relative)

class Pet(BaseModel):
	owner = ForeignKeyField(Person,related_name='pets')
	name = CharField()
	animal_type = CharField()

	def __str__(self):
		return "{0} {1} {2}".format(self.owner.name,self.name,self.animal_type)

def create_tables():
	#  User.create_table(True) and it will fail silently if the table already exists.
	if not Person.table_exists():
		Person.create_table()
	if not Pet.table_exists():
		Pet.create_table()

def create_records():
	# persons
	bob = Person(name='Bob',birthday=date(1960,1,1),is_relative=True)
	bob.save() # update database

	# create
	grandma= Person.create(name='grandma',birthday=date(1960,1,1),is_relative=False)
	herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

	grandma.name = 'Grandma L.'
	grandma.save() # update name in the database

	# pets
	bob_kitty = Pet.create(owner=bob, name='Kitty', animal_type='cat')
	herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
	herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
	herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
	
	herb_mittens.delete_instance()

	herb_fido.owner = bob
	herb_fido.save()
	bob_fido = herb_fido

def get_records():
	print('-'*30)
	for person in Person.select():
		print person.id,person.name,person.pets.count(),'pets'
		for pet in person.pets:
			print '     ',pet.name,pet.animal_type
	print('-'*30)
	for pet in Pet.select():
		print pet
	print('-'*30)
	grandma = Person.select().where(Person.name=='Grandma L.').get()
	print grandma
	grandma2 = Person.get(Person.name=='Grandma L.')
	print grandma2
	print('-'*30)
	for r in Pet.select().join(Person):
		print type(r)
		print r
	print('-'*30)
	for pet in Pet.select().join(Person).where(Person.name=='Bob'):
		print pet.name
	print('-'*30)
	for person in Person.select().order_by(Person.birthday.desc()):
	     	print person
	print('-'*30)
	for person in Person.select().where(fn.Lower(fn.Substr(Person.name,1,1))=='g'):
		print person.name
def main():
	db.connect()
	#create_tables()
	#create_records()
	get_records()
	db.close()

if __name__=="__main__":
	main()
