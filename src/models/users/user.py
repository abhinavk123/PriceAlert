import uuid

from flask import session
import src.models.users.constants as UserConstants
from src.common.database import Database
from src.common.util import Utils
import src.models.users.errors as UserErrors
from src.models.alerts.alert import Alert


class User(object):
    def __init__(self,email,password,_id = None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email,password):

        user_data = Database.find_one(UserConstants.COLLECTION,{'email':email})
        if user_data is None:
            raise UserErrors.UserNotExistsError("User does not exist.")
        if not Utils.check_hashed_password(password,user_data['password']):
            raise UserErrors.IncorrectPasswordError("Incorrect Passsword")

        return True

    @staticmethod
    def register_user(email,password):
        user_data = Database.find_one(UserConstants.COLLECTION,{'email':email})

        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("The email you used to register already Exists")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("Invalid Email Address")

        User(email,Utils.hashed_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert(UserConstants.COLLECTION,self.json())

    def json(self):
        return {
            "_id":self._id,
            "email":self.email,
            "password":self.password
        }

    def get_alerts(self):
        return Alert.find_by_email(self.email)

    @classmethod
    def find_by_email(cls,email):
        return cls(**Database.find_one(UserConstants.COLLECTION,{'email':email}))