from flask import Blueprint, render_template
from flask_login import current_user, login_required

settings_bp = Blueprint('settings', __name__)

@settings_bp.route("/settings")
@login_required  # Add this line to require login

def settings():
    return render_template("settings.html")
