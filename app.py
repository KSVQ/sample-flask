from flask import Flask
from flask import render_template

app = Flask(__name__)
# Disable caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/account")
def saccount():
    return render_template("account.html")



if __name__ == "__main__":
    app.run(debug=True)