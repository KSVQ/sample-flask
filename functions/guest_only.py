from functools import wraps
from flask import redirect, url_for
from flask_login import current_user

def guest_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('account.account'))  # Replace 'home.home' with the endpoint name of the page you want to redirect authenticated users to
        return f(*args, **kwargs)
    return decorated_function
