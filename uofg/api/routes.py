from flask import render_template, Blueprint

api = Blueprint('main', __name__)

@api.route("/")
def index():
    return render_template("index.html")