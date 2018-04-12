from flask import Blueprint, render_template

item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    return render_template("underconstruction.jinja2")

@item_blueprint.route('/load')
def load_item():
    return render_template("underconstruction.jinja2")

