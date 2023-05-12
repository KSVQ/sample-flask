from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from functions.tnxdb import TnxDB

db = TnxDB()

signup_bp = Blueprint('signup', __name__)

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password) 

        # create user in database
        db.insert_user(first_name, last_name, email, hashed_password)

        return redirect(url_for("login.login", registered=True))

    return render_template("signup.html")