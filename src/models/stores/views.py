from flask import Blueprint, render_template, request, url_for, redirect, json

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
        name = request.form['name']
        prefix = request.form['prefix']
        tag = request.form['tag_name']
        query = json.loads(request.form['query'])
        store = Store(name,prefix,tag,query)
        store.save_to_mongo()
        return redirect(url_for('.index'))

    return render_template('stores/create_store.jinja2')


@stores_blueprint.route('/edit/<string:store_id>', methods=['GET','POST'])
def edit_store(store_id):
    if request.method == 'POST':
        name = request.form['name']
        prefix = request.form['prefix']
        tag = request.form['tag_name']
        query = json.loads(request.form['query'])
        store = Store.get_by_id(store_id)
        store.name = name
        store.prefix = prefix
        store.tag_name = tag
        store.query = query
        store.save_to_mongo()
        return redirect(url_for('.index'))


    return render_template('stores/edit_store.jinja2',store = Store.get_by_id(store_id))


@stores_blueprint.route('/delete/<string:store_id>')
def delete_store(store_id):
    store = Store.get_by_id(store_id)
    store.delete()
    return redirect('/stores')