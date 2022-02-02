current state: just learning... soon starting the real thing!!!

- base: contains assets, js libs, js+css code (mostly not needed, I am using this for examples

- env: python virtual environment: =>recreate from requirements.txt

	- set this in vs code: 
		- open terminal: Ctrl+`
		- env\Scripts\activate

- frontstatic: contains examples for static frontends (no jinja2 code)
	- front0, front1, front2, .... alternative static routes (see routes in app.py)

- templates: jinja2 flask templates (jinja2: mix python code into html)
	[unused] - temp0, temp1: use local sqlalchemy db test.db 
	- todo, car: uses postgres db:
		- to run locally: in app.py set ENV='dev' (needs local Postgres installation)
		- run on heroku: in app.py set ENV='prod' (is persistent!!!!)

- app.py is the newest flask interface
	- app_examples: app0, app1, ... previous flask app examples

[unused] - test.db is the local database (sqlalchemy)

=>also see howto.txt for details

=>recommended tutorials:
- https://www.youtube.com/watch?v=Z1RJmh_OqeA
- https://www.youtube.com/watch?v=w25ea_I89iM











