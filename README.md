1. directory structure:

- base: contains lots of assets most of which not needed, and 3rd party javascript libs in alibs

- env: python virtual environment: 
	set this in vs code: 
		- open terminal: Ctrl+`
		- >env\Scripts\activate

- front0: contains js and css code base. 
	- most of it not needed, but some very useful (base.js)
	- also, index.html is a static starter file for html that loads most important files from code base

- front1, front2, .... alternative static routes (see routes in app.py)

- templates: jinja 2 flask templates
	- jinja2 code allows mixing python code into html files, eg. to load data from db...
	- css and js dirs contain file only used in templates



app.py is the full flask interface with routes and database code

test.db is the database (sqlalchemy)












