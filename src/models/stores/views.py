from flask import Blueprint, render_template

stores_blueprint = Blueprint('stores', __name__)

@stores_blueprint.route('/')
def index():
    return render_template("underconstruction.jinja2")

@stores_blueprint.route('/stores/<string:name>')
def store_page(name):
    return render_template("underconstruction.jinja2")
