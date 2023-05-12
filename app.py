from flask import Flask
from flask_login import LoginManager

from functions.user import User
from functions.tnxdb import TnxDB

from routes import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'Tnx4U2c!'

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login.login'  # Configure the login view

@login_manager.user_loader
def load_user(user_id):
    db = TnxDB()
    user_data = db.get_user_by_id(user_id)
    if user_data:
        return User(user_data)
    else:
        return None

for blueprint in route_blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)
