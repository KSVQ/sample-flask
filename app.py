from flask import Flask
from flask import render_template

app = Flask(__name__)
# Disable caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
    return render_template("home.html")
    # if logged in, redirect to dashboard
    # return render_template("dashboard.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)