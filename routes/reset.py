# login.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required
from werkzeug.security import check_password_hash
from functions.tnxdb import TnxDB
from functions.user import User

db = TnxDB()

reset_bp = Blueprint('reset', __name__)

@reset_bp.route("/reset", methods=["GET", "POST"])
@login_required  # Add this line to require login

def reset():
    # return redirect(url_for('home.home'))
    # if request.method == 'POST':
    #     email = request.form['email']
    #     password = request.form['password']
    #     user = db.get_user_by_email(email)
    #     if not user:
    #         flash('User does not exist.')
    #         return redirect(url_for('login.login', user="noUser"))
    #     elif not check_password_hash(user[4], password):
    #         flash('Incorrect password.')
    #         return redirect(url_for('login.login', user="noPass"))
    #     else:
    #         # Successful login
    #         user_obj = User(user)
    #         login_user(user_obj)  # Set the user as logged in
    #         print(login_user(user_obj))
    #         return redirect(url_for('home.home'))

    # registered = request.args.get("registered")
    # if registered is not None:
    #     flash("Account created successfully!", "success")


    return render_template("reset.html")
