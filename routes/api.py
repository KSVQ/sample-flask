from flask import jsonify, Blueprint
from flask_login import current_user, login_required

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/data')
@login_required  # Add this line to require login
def get_data():
    # code to fetch data
    # data = {"message": "Hello, world!"}
    
    # Make sure to extract only the required fields from the current_user object, and not the entire object
    data = {
        "id": current_user.id,
        "name": current_user.first_name,
        "surname": current_user.last_name,
        "email": current_user.email,
        "role": current_user.role,
        "theme": current_user.theme,
        # Add any other required fields here
    }
    print(data)
    
    # return jsonify(data)
    return jsonify(data)
