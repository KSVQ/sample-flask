from flask import jsonify, Blueprint, request
from flask_login import current_user, login_required
from functions.api_handler import APIHandler

api_handler = APIHandler()

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/<string:method_name>', methods=['GET', 'POST'])
@login_required
def api(method_name):

    user = {
        "id": current_user.id,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email,
        "role": current_user.role,
        "theme": current_user.theme
    }


    if request.method == 'POST':
        data = request.get_json()
        if method_name == "set_theme":
            theme = data.get('theme')
            if theme is not None:
                if api_handler.set_theme(theme):
                    return jsonify({'status': 'Theme updated successfully'})
                else:
                    return jsonify({'error': 'Failed to update theme.'}), 500
            else:
                return jsonify({'error': 'Theme not provided in request.'}), 400


    if request.method == 'GET':
        if method_name == "logged_in":
            response = api_handler.logged_in()
            return jsonify(user)
        
        return jsonify({'error': 'Invalid method name.'}), 400



# if theme:
#     current_user.theme = theme
#     # return jsonify(data)
#     return jsonify({'message': 'User theme preference updated.'})
# else:
#     return jsonify({'error': 'Invalid theme value.'}), 400