from flask import Flask
from routes import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

for blueprint in route_blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)