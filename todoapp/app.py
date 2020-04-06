from flask import ( Flask, render_template, request, 
redirect, url_for, jsonify, abort )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fsteffenino:@localhost:5432/todoapp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'),
                             nullable=False)

    def __reps__(self):
        return f'<Todo {self.id} {self.description} {self.completed} {self.list_id}>'

class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)


@app.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    error = False
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify({ 'success': True })

@app.route('/todo/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    newCompleted = request.get_json()['completed']
    error = False
    try:
        todo = Todo.query.get(todo_id)
        todo.completed = newCompleted
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return redirect(url_for('index'))


@app.route('/todo/create', methods=['POST'])
def create():
    desc = request.get_json()['description']
    error = False
    try:
        todo = Todo(description=desc)
        db.session.add(todo)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify({
            'description' : desc
        })

@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    lists = TodoList.query.order_by('id').all()
    active = TodoList.query.get(list_id)
    data = Todo.query.filter_by(list_id=list_id).order_by('id').all()
    return render_template('index.html', active=active, category=lists, data=data)



@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))