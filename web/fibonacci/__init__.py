
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import app_config


db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'redis'})

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    cache.init_app(app)
    migrate = Migrate(app, db)

    from .fib import fib as fib_blueprint
    from .health import health as health_blueprint
    app.register_blueprint(fib_blueprint, url_prefix='/fib')
    app.register_blueprint(health_blueprint)
    return app