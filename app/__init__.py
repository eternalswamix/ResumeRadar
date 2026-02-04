from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from app.config import Config
from datetime import datetime
import os

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY

    # Custom Jinja2 filters
    app.jinja_env.filters['strptime'] = lambda value, fmt: datetime.strptime(value, fmt)
    app.jinja_env.filters['strftime'] = lambda value, fmt: value.strftime(fmt)

    # Register blueprints (Delayed imports to avoid circular dependency)
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.resume_routes import resume_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(resume_bp)

    # Trust Vercel's proxy headers
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    return app
