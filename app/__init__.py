from flask import Flask
from .routes import book_routes
from .extensions import db, migrate, cache
from flasgger import Swagger
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_HOST'] = 'localhost'
    app.config['CACHE_REDIS_PORT'] = 6379

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    Swagger(app)
    app.register_blueprint(book_routes)

    return app
