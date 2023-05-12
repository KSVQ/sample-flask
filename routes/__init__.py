from .home import home_bp
from .copywriter import copywriter_bp
from .login import login_bp
from .signup import signup_bp
from .settings import settings_bp
from .account import account_bp
from .faq import faq_bp
from .pricing import pricing_bp
from .about import about_bp
from .logout import logout_bp
from .reset import reset_bp
from .api import api_bp

route_blueprints = [
    home_bp, copywriter_bp, login_bp, 
    signup_bp, settings_bp, account_bp, 
    faq_bp, pricing_bp, about_bp, 
    logout_bp, reset_bp, api_bp
]