from flask import Blueprint, request, session, url_for, redirect, render_template

from src.models.users import errors
from src.models.users.user import User

user_blueprint = Blueprint('users',__name__)

@user_blueprint.route('/login',methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email,password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except errors.UserErrors as e:
            return e.message

    return render_template("users/login.html")





@user_blueprint.route('/register',methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email,password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except errors.UserErrors as e:
            return e.message

    return render_template("users/register.html")

@user_blueprint.route('/logout')
def logout_user():
    pass

@user_blueprint.route('/alters')
def user_alerts():
    return "This is a alter page"

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
