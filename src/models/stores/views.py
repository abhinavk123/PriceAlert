from flask import Blueprint, render_template, request, url_for

from src.models.stores.store import Store

stores_blueprint = Blueprint('stores', __name__)

@stores_blueprint.route('/')
def index():
    stores = Store.find_all()
    return render_template("stores/store_index.jinja2", stores=stores)

@stores_blueprint.route('/store/<string:store_id>')
def store_page(store_id):
    store = Store.get_by_id(store_id)
    return render_template("stores/store.jinja2",store= store)

@stores_blueprint.route('/new',methods=['GET','POST'])
def create_store():
    if request.method == 'POST':
        pass

    return "This is store creation page "

@stores_blueprint.route('/edit',methods=['GET','POST'])
def edit_store():
    if request.method == 'POST':
        pass

    return "This is store edit page "

@stores_blueprint.route('/delete/<string:store_id')
def delete_store():
    return "delete store"