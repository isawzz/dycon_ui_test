import os
from flask import Flask, render_template, url_for, request, send_from_directory, redirect
from send_mail import send_mail

app = Flask(__name__, static_url_path='', static_folder='')

#region database
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

ENV = 'prod' #prod to run on Heroku, dev to run locally (needs Postgres installed for / routes)
if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres: @localhost:5434/lexus'
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://emjonsyhpsrwsm:52ffe4ea7e9df56ef4a318d7100ce2604150edee57b63cc17f6b4beb94af2fd4@ec2-54-157-15-228.compute-1.amazonaws.com:5432/d17abf8v9ivuhc'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
	__tablename__ = 'todo'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __init__(self, content):
		self.content = content

	def __repr__(self):
		return '<Task %r>' % self.id

class Feedback(db.Model):
	__tablename__ = 'feedback'
	id = db.Column(db.Integer, primary_key=True)
	customer = db.Column(db.String(200), unique=True)
	dealer = db.Column(db.String(200))
	rating = db.Column(db.Integer)
	comments = db.Column(db.Text())

	def __init__(self, customer, dealer, rating, comments):
		self.customer = customer
		self.dealer = dealer
		self.rating = rating
		self.comments = comments

#endregion

#region jinja2 routes (flask template) routes: mix python into html

@app.route('/')
def mainmenu():
	return render_template('index.html')

#region example 1: todolist
@app.route('/todo', methods=['POST', 'GET'])
def template():
	if request.method == 'POST':
		#return 'Hello!' #works when click auf 'Add Task' button
		#add posted data as new task
		task_content = request.form['content'] # should be id of input (see index.html)
		new_task = Todo(content=task_content)
		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/todo')
		except:
			return 'error adding task!'
	else:
		#show tasks from test.db in templates/index.html
		tasks = Todo.query.order_by(Todo.date_created).all() #.first(), 
		return render_template('todolist/index.html', tasks=tasks)

@app.route('/deltodo/<int:id>')
def del_todo(id):
	task_to_delete = Todo.query.get_or_404(id)
	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/todo')
	except:
		return 'There was a problem deleting that task'

@app.route('/uptodo/<int:id>', methods=['GET', 'POST'])
def update(id):
	task = Todo.query.get_or_404(id)
	if request.method == 'POST':
		task.content = request.form['content']
		try:
			db.session.commit()
			return redirect('/todo')
		except:
			return 'There was an issue updating your task'
	else:
		return render_template('todolist/update.html', task=task)
#endregion todolist

#region example 2: car
@app.route('/car')
def car_index():
	return render_template('car/index.html')

@app.route('/carsubmit', methods=['POST'])
def car_submit():
	if request.method == 'POST':
		customer = request.form['customer']
		dealer = request.form['dealer']
		rating = request.form['rating']
		comments = request.form['comments']
		print(customer, dealer, rating, comments)
		if customer == '' or dealer == '':
			return render_template('car/index.html', message='Please enter required fields')
		if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
			data = Feedback(customer, dealer, rating, comments)
			db.session.add(data)
			db.session.commit()
			send_mail(customer, dealer, rating, comments)
			return render_template('car/success.html')
		return render_template('car/index.html', message='You have already submitted feedback')
#endregion example 2: card dealer feedback
#endregion

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

if __name__ == "__main__":
	app.run(debug=True,port=8000)












