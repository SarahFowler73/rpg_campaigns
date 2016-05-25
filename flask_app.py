from flask import Flask, render_template, g
from flask.ext.login import LoginManager

import models

DEBUG = True
PORT = 8888
HOST = 'localhost'


app = Flask(__name__)
app.secret_key = ""

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close db conn after request"""
    g.db.close()
    return response


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT, host=HOST)
