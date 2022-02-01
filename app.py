from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'
if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres: @localhost:5434/lexus'
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://emjonsyhpsrwsm:52ffe4ea7e9df56ef4a318d7100ce2604150edee57b63cc17f6b4beb94af2fd4@ec2-54-157-15-228.compute-1.amazonaws.com:5432/d17abf8v9ivuhc'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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


@app.route('/')
def index():
	return render_template('temp2/index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		customer = request.form['customer']
		dealer = request.form['dealer']
		rating = request.form['rating']
		comments = request.form['comments']
		print(customer, dealer, rating, comments)
		if customer == '' or dealer == '':
			return render_template('temp2/index.html', message='Please enter required fields')
		if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
			data = Feedback(customer, dealer, rating, comments)
			db.session.add(data)
			db.session.commit()
			send_mail(customer, dealer, rating, comments)
			return render_template('temp2/success.html')
		return render_template('temp2/index.html', message='You have already submitted feedback')

if __name__ == '__main__':
	app.run()
