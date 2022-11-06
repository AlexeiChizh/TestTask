

from peewee import *

conn = SqliteDatabase('ORM.sqlite')


class Personal(Model):
	id = PrimaryKeyField(column_name = 'personal_id', unique = True)
	name = CharField(column_name = 'name')
	surname = CharField(column_name = 'surname')
	skill = CharField(column_name = 'skill')

	class Meta:
		database = conn


class Project(Model):
	id = PrimaryKeyField(column_name ='project_id', unique = True)
	pr_name = CharField(column_name = 'project_name')

	class Meta:
		database = conn


class Object(Model):
	id = PrimaryKeyField(column_name ='object_id', unique = True)
	ob_name = CharField(column_name = 'object_name')
	ob_region = CharField(column_name = 'object_region')
	ob_subregion = CharField(column_name = 'object_subregion')
	ob_city = CharField(column_name = 'object_city')
	ob_local_address = CharField(column_name = 'object_address')

	class Meta:
		database = conn


class Accordance(Model):
	personal_id = ForeignKeyField(Personal)
	object_id = ForeignKeyField(Object)
	project_id = ForeignKeyField(Project)

	class Meta:
		database = conn


Personal.create_table()
Project.create_table()
Object.create_table()
Accordance.create_table()


Personals = [
 {'id': 1, 'name': 'Ivan', 'surname': 'Ivanov', 'skill': 'electronics'},
 {'id': 2, 'name': 'Petr', 'surname': 'Petrov', 'skill': 'electrical engineer'},
 {'id': 3, 'name': 'Sidor', 'surname': 'Sidorov', 'skill': 'system administrator'},
 {'id': 4, 'name': 'Fedor', 'surname': 'Fedorov', 'skill': 'consultant'}
]

Personal.insert_many(Personals).execute()



Personals_M = (Personal.select().where(Personal.skill == 'consultant'))
for a in Personals_M:
	print(a.name, a.surname)


Projects = [
{'id': 1, 'pr_name':'computer repair'},
{'id': 2, 'pr_name':'softwear installation'},
{'id': 3, 'pr_name':'server repair'},
{'id': 4, 'pr_name':'low-current electrics'},
{'id': 5, 'pr_name':'user consultation'}
]

Project.insert_many(Projects).execute()

Objects = [
{'id': 1, 'ob_name':'Ilon Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Moscow', 'ob_local_address':'Leninsky,45'},
{'id': 2, 'ob_name':'Mask Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Domodedovo', 'ob_local_address':'Pervaya, 4'},
{'id': 3, 'ob_name':'Donald Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Moscow', 'ob_local_address':'Dmitrovskoe, 90'},
{'id': 4, 'ob_name':'Trump Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Podolsk', 'ob_local_address':'Industrialnaya, 45'},
{'id': 5, 'ob_name':'Blackmore Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Odintsovo', 'ob_local_address':'Vesennaya, 145'},
{'id': 6, 'ob_name':'Derris Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Moscow', 'ob_local_address':'Kashirskoe, 45'},
{'id': 7, 'ob_name':'Marcus Limited', 'ob_region':'Russia', 'ob_subregion':'Moscow region', 'ob_city':'Golitsyno', 'ob_local_address':'Lesnaya, 45'}
]

Object.insert_many(Objects).execute()

per = Personal.select()
o = Object.select()
p = Project.select()

Accordances = [
{'personal_id': per[0], 'object_id': o[0], 'project_id': p[0]},
{'personal_id': per[1], 'object_id': o[1], 'project_id': p[1]},
{'personal_id': per[2], 'object_id': o[2], 'project_id': p[0]},
{'personal_id': per[1], 'object_id': o[3], 'project_id': p[0]},
{'personal_id': per[2], 'object_id': o[4], 'project_id': p[2]},
{'personal_id': per[0], 'object_id': o[5], 'project_id': p[3]},
{'personal_id': per[1], 'object_id': o[6], 'project_id': p[4]}
]

Accordance.insert_many(Accordances).execute()

Oelec = Object.select().join(Accordance).where(Accordance.project_id == 4)
for a in Oelec:
	print(a.ob_name)

Ob_moscow = Object.select().where(Object.ob_city == 'Moscow')
for c in Ob_moscow:
	print(c.ob_name)



