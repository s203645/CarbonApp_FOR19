from flask import Flask
application = Flask(__name__)

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.developer.routes import developer
from capp.cv.routes import cv
from capp.users.routes import users


application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(developer)
application.register_blueprint(cv)
application.register_blueprint(users)