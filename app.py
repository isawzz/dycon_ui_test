import os
from flask import Flask, render_template, request, send_from_directory

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
@app.route('/')
def index():
	return send_from_directory('front', 'index.html')
@app.route('/1')
def index1():
	return send_from_directory('front1', 'index.html')
@app.route('/2')
def index2():
	return send_from_directory('front2', 'index.html')

#region jinja 2 (flask template) routes: mix python into html
@app.route('/templates', methods=['POST', 'GET'])
def template():
	if request.method == 'POST':
		return 'Hello!'
	else:
		return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)











