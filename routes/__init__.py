from .home import home_bp
from .login import login_bp
from .signup import signup_bp
from .settings import settings_bp
from .account import account_bp
from .faq import faq_bp
from .pricing import pricing_bp
from .about import about_bp

route_blueprints = [
    home_bp, login_bp, signup_bp,
    settings_bp, account_bp, faq_bp,
    pricing_bp, about_bp
]