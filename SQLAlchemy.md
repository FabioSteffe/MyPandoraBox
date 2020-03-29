## SQLAlchemy

ORM (Object relational mapping) lib for python.  

```
class Todos (db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  completed = db.Column(db.Boolean, nullable=false, default=False)
```

with the ORM class we can do things that usually we do with SQL using pre-existing methods:

```
Todos.query.all() # SELECT * from Todos;

```

Layers of SQLAlchemy
- DBAPI
- The Dialect
- The Connection Pool
- The Engine
- SQL Expressions
- SQLAlchemy ORM 

class in python:
```
class Human:
  def __init__(self, first_name, last_name, age):
    self.name = fisrt_name
    self.family = last_name
    self.age = age
    
sarah = Human('sarah','parker',40)
```

in ORM:
- classes = table
- object = record
- attribute = colum

Flask and SQLAlchemy:
```
pip3 install flask
pip3 install flask-sqlalchemy
```

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 'dialect://username:password@ip:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fsteffenino:@localhost:5432/fsteffenino'
db = SQLAlchemy(app) 


@app.route('/')
def index():
    return 'Hello World!'
```

- `db.Model` lets us create and manipulate data models
- `db.session` lets us create and manipulate database transactions

Declaring classes
- `class MyModel(db.Model)` will inherit from db.Model.  
- By inheriting from `db.Model`, we map from our classes to tables via SQLAlchemy ORM.  
Defining columns
- Within our class, we declare attributes equal to `db.Column(...)`.  
- `db.Column` takes `<datatype>, <primary_key?>, <constraint?>, <default?>`.  
Table naming
- By default, SQLAlchemy will pick the name of the table for you, setting it equal to the lower-case version of your class's name. Otherwise, we set the name of the table using `__tablename__ = 'my_custom_table_name'`.

```
class Person (db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
```

create tables:
- `db.create_all()` will create all the previously defined tables if they are not existing

some basic commands:
- `Person.query.first()`
- `Person.query.all()`
- `Person.query.count()`
- `Person.query.filter(Person.name == 'Fabio').all()`
- `Person.query.filter(Person.name == 'Fabio').first()`
- `Person.query.filter_by(name = 'Fabio').all()`
- `Person.query.filter_by(name = 'Fabio', city='boston').all()`


SQLAlchemy data types:
- Integer
- String(size)
- Text
- DateTime
- Float
- Boolean
- PickleType
- LargeBinary

define constraints:
```
class User(db.Model):
  ...
  name = db.Column(db.String(), nullable=False, unique=True)
  
class Product(db.Model):
  ...
  price = db.Column(db.Float, db.CheckConstraint('price>0'))
```

cheatsheet: https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-sqlalchemy.rst#set-a-database-url 

insert data:
```
person1 = Person(name='bobby')
person2 = Person(name='marlon')
db.session.add(person1)
db.session.add_all([person1, person2])
db.session.commmit()
db.session.rollback()
```

filtering:
- equals: query.filter(User.name == 'ed')
- not equals: query.filter(User.name != 'ed')
- LIKE: query.filter(User.name.like('%ed%'))
- ILIKE (case-insensitive LIKE): query.filter(User.name.ilike('%ed%'))
- IN: query.filter(User.name.in_(['ed', 'wendy', 'jack']))
- NOT IN: query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
- IS NULL: query.filter(User.name == None)
- IS NOT NULL: query.filter(User.name != None)
- AND: query.filter(User.name == 'ed', User.fullname == 'Ed Jones') or chain filter methods together.
- OR: query.filter(User.name == 'a' | User.name == 'b')
- MATCH: query.filter(User.name.match('wendy'))

Ordering:
- Person.order_by(db.desc(Person.name))
- Person.order_by(Person.name)

Get from key:
- Person.query.get(key)

Delete:
- Person.query.filter_by(name='fabio').delete()

Join:
- Person.query.join('cars')

Update:
- person1.name = 'gino'

CRUD:
- CREATE
- READ
- UPDATE
- DELETE




