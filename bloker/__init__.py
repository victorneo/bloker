from flask import Flask
from .core import db


def create_app(config='settings'):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from .posts.views import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    return app