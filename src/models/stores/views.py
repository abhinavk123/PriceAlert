from flask import Blueprint, render_template

from src.models.stores.store import Store

stores_blueprint = Blueprint('stores', __name__)

@stores_blueprint.route('/')
def index():
    stores = Store.find_all()
    return render_template("stores/store.jinja2",stores=stores)

@stores_blueprint.route('/stores/<string:name>')
def store_page(name):
    return render_template("underconstruction.jinja2")

@stores_blueprint.route('/create_store')
def create_store():
    pass