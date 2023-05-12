# home.py
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("copywriter.copywriter"))
    else:
        return render_template("home.html")
