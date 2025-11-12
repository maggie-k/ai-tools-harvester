from flask import Flask
import pandas as pd

def create_app():
	app= Flask(__name__)

	app.config['SECRET_KEY']= 'AI'

	app.df = pd.read_csv("data/ai_tools.csv")

	from app.routes.main import main
	app.register_blueprint(main)

	return app