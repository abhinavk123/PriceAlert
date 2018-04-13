from flask import Blueprint, render_template, request

from src.models.alerts.alert import Alert

alert_blueprint = Blueprint('alerts',__name__)


@alert_blueprint.route('/')
def index():
    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/new',methods=['GET','POST'])
def create_alert():
    if request.method == 'POST':
        pass

    return render_template('alerts/create_alert.jinja2')

    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    return render_template("underconstruction.jinja2")


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
    alert = Alert.find_by_id(alert_id)
    return render_template('alerts/alert.jinja2',alert=alert)


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    return render_template("underconstruction.jinja2")