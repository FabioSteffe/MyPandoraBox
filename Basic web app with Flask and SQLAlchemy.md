# Basic web app with Flask and SQLAlchemy

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

## Flask

basic hello world with flask
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello world'
```

run flask app (default method)
```
export FLASK_ENV=development # enables live reload
export FLASK_DEBUG=true # enables live reload
FLASK_APP=app.py flask run
FLASK_APP=app.py FLASK_DEBUG=true flask run # enable debug mode
```

run flask app (with main):
- define main in app.py
```
if __name__ == '__main__':
  app.run()
```
- run using python3 app.py

MVC architechture
- MODEL : manage data
- VIEW : handles display
- CONTROLLER : controls the logic

Getting user data from application/json request
```
data_string = request.data
data_dictionary = json.loads(data_string)
```

Getting user data from form submission
```
username = request.form.get('username')
password = request.form.get('password')
```

Getting user data from parameters
```
username = request.args.get('username')
```

Basic todo list app with flask
```
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fsteffenino:@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __reps__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/todo/create', methods=['POST'])
def create():
    desc = request.form.get('description')
    
    todo = Todo(description=desc)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/')
def index():

    data = Todo.query.all()
    return render_template('index.html', data=data)
```
basic html page
```
<div>
    <head>
        <title>
            TO-DO App
        </title>
    </head>
    <body>
        <form action="/todo/create" method="post">
            <label for="create-todo">Create todo</label>
            <input type="text" value="" id="desc" name="description" />
            <input type="submit" value="Submit" />
         </form>
        <ul>
            {% for d in data %}
            <li>
                {{ d.description }}
            </li>
            {% endfor %}
        </ul>
        
    </body>
</div>
```

We can request data from server synchronously or asynchronously.  
AJAX is used for async requests.  
- XMLHttpRequest
- Fetch (modern)
  - `fetch(<url-route>, <object of request parameters>)`

```
fetch( '/request', {
  method: 'POST',
  body: JSON.stringify({
    'description' : 'bla bla'
  }),
  headers: {
    'content-type' : 'application/json'
  }
});
```


update in sqlalchemy:
```
user = User.query.get(id)
user.name = 'gianni'
db.session.commit()
```

delete in sqlalchemy:
```
todo = Todo.query.get(todo_id) 
db.session.delete(todo) # or...
Todo.query.filter_by(id=todo_id).delete()
db.session.commit()
```

##### Relationship in SQLAlchemy.  

SQLAlchemy configures the settings between model relationships once, and generates JOIN statements for us whenever we need them.
- db.relationship is an interface offered in SQLAlchemy to provide and configure a mapped relationship between two models.
- db.relationship is defined on the parent model, and it sets:
  - the name of its children (e.g. children), for example parent1.children
  - the name of a parent on a child using the backref, for example child1.my_amazing_parent

db.relationship
- Allows SQLAlchemy to identity relationships between models
- Links relationships with backrefs (child1.some_parent)
- Configures relationship dynamics between parents and children, including options like `lazy`, `collection_class`, and `cascade`

- db.relationship does not set up foreign key constraints for you. We need to add a column, some_parent_id, on the child model that has a foreign key constraint
- Whereas we set db.relationship on the parent model, we set the foreign key constraint on the child model.
- A foreign key constraint prefers referential integrity from one table to another, by ensuring that the foreign key column always maps a primary key in the foreign table.

`db.ForeignKey`
- Option in db.column to specify a foreign key constraint, referring to the primary key of the other table / model
- Gets defined on the Child model


```
class Parent(db.Model):
  id = ...
  name = ...
  children = db.relationship('Child', 
                              backref='the_parent',
                              lazy=True
                              collection_class = list, # dictionary, set
                              cascade = 'save-update' # all, delete-orphan
                              )
```

SQLAlchemy is joining tables automatically, but when?   
- Lazy
  - only when needed 
  - when `child.the_parent` is called
  - lazy='select'
- Eager
  - all join done at once in a giant expensive operation
  - lazy='joined'

Foreign key in child:
```
class Parent(db.Model):
  __tablename__ = 'some_parents'
  id = db.Column(db.Integer, primary_key=True)
  ...

class Child(db.Model):
  id = ...
  name = ...
  some_parent_id = db.Column(db.Integer, db.ForeignKey('some_parents.id'),
                             nullable=False)
```

Many to Many relation:
```
order_items = db.Table('order_items',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String(), nullable=False)
  products = db.relationship('Product', secondary=order_items,
      backref=db.backref('orders', lazy=True))

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
```




###### Schema migration in flask app

```
migrations/
  add_tables_0001.py
  add_column_to_todo_0002.py
```
- db migrate : migration script
- db upgrade : apply migration
- db downgrade : rollback

db.create_all() is not used when we are using migrations.  

libraries doing the job:
- Flask-Migrate(flask_migrate)
- Flask-Script(flask_script)

- `flask db init` initialise migration dir
- `flask db migrate` creates migration files - to be run every time we modify the model
- `flask db upgrade` upgrade the db
- `flask db downgrade` rollback the changes

```
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fsteffenino:@localhost:5432/todoapp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

```













