from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash

signup_bp = Blueprint('signup', __name__)

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password) 

        flash("Account created successfully!", "success")
        # print("Account created successfully!", "success")

        return redirect(url_for("login.login"))

    return render_template("signup.html")