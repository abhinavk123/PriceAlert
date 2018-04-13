from flask import Blueprint, request, session, url_for, redirect, render_template

from src.models.alerts.alert import Alert
from src.models.users import errors
from src.models.users.user import User

user_blueprint = Blueprint('users',__name__)

@user_blueprint.route('/login',methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email,password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except errors.UserErrors as e:
            return e.message

    return render_template("users/login.jinja2")





@user_blueprint.route('/register',methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email,password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except errors.UserErrors as e:
            return e.message

    return render_template("users/register.jinja2")

@user_blueprint.route('/logout')
def logout_user():
    session['email']=None
    return redirect(url_for('home'))

@user_blueprint.route('/alters')
def user_alerts():
    user = User.find_by_email(session['email'])
    alerts = user.get_alerts()
    return render_template("users/alerts.jinja2",alerts=alerts)

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    return render_template("underconstruction.jinja2")

