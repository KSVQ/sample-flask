# login.py
from flask import Blueprint, render_template, request, flash

login_bp = Blueprint('login', __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # handle login form submission
        pass

    registered = request.args.get("registered")
    if registered is not None:
        flash("Account created successfully!", "success")


    return render_template("login.html")
