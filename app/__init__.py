from flask import Flask

def create_app():
	app= Flask(__name__)

	app.secret_key= os.environ.get("SECRET_KEY")		

	from app.routes.main import main
	app.register_blueprint(main)

	return app
