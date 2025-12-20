from flask import Flask

def create_app():
	app= Flask(__name__)

	app.config['SECRET_KEY']= 'AI'		

	from app.routes.main import main
	app.register_blueprint(main)

	return app


#Invert the dependency
#Instead of db importing from app, pass what it needs:
#db.py 
#def init_db(app)
# app.py 
#from db import init_db 
#init_db(app) 

#Import inside the function
#def db():
		#from app.models import init_db
		#init_db()