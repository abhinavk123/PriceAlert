from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_matcher = re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
        return True if email_matcher.match(email) else False


    @staticmethod
    def hashed_password(password):

        return  pbkdf2_sha512.encrypt(password)
    @staticmethod
    def check_hashed_password(password,hashed_password):


        return pbkdf2_sha512.verify(password,hashed_password)