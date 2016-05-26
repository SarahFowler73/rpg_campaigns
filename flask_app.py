from flask import (Flask, render_template, g, flash,
                  redirect, url_for)
from flask.ext.login import LoginManager

import models
import forms

DEBUG = True
PORT = 8888
HOST = 'localhost'


app = Flask(__name__)
app.secret_key = "93048209840801973jhkjklm1l2k;jilo2j1iophf"

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


# Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash("Registration complete!", "success")
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT, host=HOST)
