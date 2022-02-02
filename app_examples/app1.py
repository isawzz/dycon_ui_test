import os
from flask import Flask, render_template, url_for, request, send_from_directory, redirect

app = Flask(__name__, static_url_path='', static_folder='')

#region database
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #relative path, //// would be absolute path
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


#endregion database

#region static routes
@app.route('/0')
def index0():
	return send_from_directory('frontstatic/front0', 'index.html')
@app.route('/1')
def index1():
	return send_from_directory('frontstatic/front1', 'index.html')
@app.route('/2')
def index2():
	return send_from_directory('frontstatic/front2', 'index.html')

#endregion

#region jinja 2 (flask template) routes: mix python into html

@app.route('/', methods=['POST', 'GET'])
def template():
	if request.method == 'POST':
		#return 'Hello!' #works when click auf 'Add Task' button
		#add posted data as new task
		task_content = request.form['content'] # should be id of input (see index.html)
		new_task = Todo(content=task_content)
		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'error adding task!'
	else:
		#show tasks from test.db in templates/index.html
		tasks = Todo.query.order_by(Todo.date_created).all() #.first(), 
		return render_template('temp0/index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)
	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	task = Todo.query.get_or_404(id)
	if request.method == 'POST':
		task.content = request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue updating your task'
	else:
		return render_template('temp0/update.html', task=task)



if __name__ == "__main__":
	app.run(debug=True,port=8000)












