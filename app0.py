import os
from flask import Flask, request, send_from_directory

# template_dir = os.path.join(os.path.dirname(__file__), 'frontend')
# print('index.html should be in',template_dir)

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def index():
	return send_from_directory('front', 'index.html')
@app.route('/1')
def index1():
	return send_from_directory('front1', 'index.html')
@app.route('/2')
def index2():
	return send_from_directory('front2', 'index.html')

if __name__ == "__main__":
	app.run(debug=True)












