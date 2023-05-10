from flask import Blueprint, render_template, request, flash, redirect, url_for

signup_bp = Blueprint('signup', __name__)

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")