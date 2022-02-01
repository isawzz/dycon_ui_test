current state: just learning... soon starting the real thing!!!

- base: contains assets, js libs, js+css code (mostly not needed, I am using this for examples

- env: python virtual environment: =>recreate from requirements.txt

	- set this in vs code: 
		- open terminal: Ctrl+`
		- env\Scripts\activate

- frontstatic: contains examples for static frontends (no jinja2 code)
	- front0, front1, front2, .... alternative static routes (see routes in app.py)

- templates: jinja2 flask templates (jinja2: mix python code into html)
	- temp0, temp1: use local sqlalchemy db test.db
	- temp2: uses postgres db (if ENV='dev' need to install Postgres locally): provides heroku data persistence!!!!

- app.py is the newest flask interface, currently routing to temp2 example (works on heroku) 
	- app0, app1, ... previous flask apps for fraontstatic examples and temp0/1 examples

- test.db is the local database (sqlalchemy)













