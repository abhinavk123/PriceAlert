from flask import Blueprint, render_template

alert_blueprint = Blueprint('alerts',__name__)


@alert_blueprint.route('/')
def index():
    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/new',methods=['POST'])
def create_alert():
    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    return render_template("underconstruction.jinja2")