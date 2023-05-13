# api_handler.py
from flask_login import current_user
from functions.tnxdb import TnxDB

db = TnxDB()

class APIHandler:

    def __init__(self):
        # Initialize any necessary attributes or dependencies here
        pass

    def logged_in(self):
        # Handle the request and return a response
        if current_user.is_authenticated:
            return True

    def set_theme(self, theme):
        if current_user.is_authenticated:
            if db.update_user_theme(current_user.id, theme):
                return True
            else:
                return False
        else:
            return False