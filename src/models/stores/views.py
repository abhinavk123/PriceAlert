from flask import Blueprint

stores_blueprint = Blueprint('stores', __name__)

@stores_blueprint.route('/store/<string:name>')
def store_page(name):
    pass
