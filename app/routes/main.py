from flask import Blueprint, render_template, request, current_app
from app.recommender import recommend_tools
#from app.models import init_db

#init_db()

main= Blueprint('main',__name__)

@main.route('/', methods=["GET", "POST"])
def index():
	recommendations= []
	if request.method == "POST":
		user_input= request.form.get("need")
		recommendations= recommend_tools(user_input) 

	return render_template('index.html', recommendations=recommendations)
