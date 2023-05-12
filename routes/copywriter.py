# copywriter.py
from flask import Blueprint, render_template
from flask_login import current_user, login_required

data = []
for i in range(1, 13):
    data.append({"file_name": f"dummy{i}.txt", "clean_file_name": f"Dummy File {i}"})


copywriter_bp = Blueprint('copywriter', __name__)

@copywriter_bp.route("/copywriter")
@login_required  # Add this line to require login
def copywriter():
    return render_template("copywriter.html", data=data)