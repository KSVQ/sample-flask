# login.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash
from functions.guest_only import guest_only
from functions.tnxdb import TnxDB
from functions.user import User

db = TnxDB()

login_bp = Blueprint('login', __name__)

@login_bp.route("/login", methods=["GET", "POST"])
@guest_only
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.get_user_by_email(email)
        if not user:
            flash('User does not exist.')
            return redirect(url_for('login.login', user="noUser"))
        elif not check_password_hash(user[4], password):
            flash('Incorrect password.')
            return redirect(url_for('login.login', user="noPass"))
        else:
            # Successful login
            user_obj = User(user)
            login_user(user_obj)  # Set the user as logged in
            # Check if there's a 'next' parameter in the request arguments
            next_page = request.args.get('next')
            # If 'next' is present, redirect the user to the intended URL
            if next_page:
                return redirect(next_page)
            # Otherwise, redirect the user to the default page (e.g., home page)
            else:
                return redirect(url_for('home.home'))

    registered = request.args.get("registered")
    if registered is not None:
        flash("Account created successfully!", "success")

    return render_template("login.html")
