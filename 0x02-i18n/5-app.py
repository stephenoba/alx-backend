#!/usr/bin/env python3
"""
Basic Flask app that creates a single / route.
"""
from typing import Union
from flask import g
from flask import Flask, render_template
from flask import request
from flask_babel import Babel, _


class Config:
    """
    Config for flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Get User's locale from AcceptLanguagesx header
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """
    Get a user from users dictionary of None
    """
    user = None
    login_as = request.args.get('login_as', None)
    if login_as:
        user = users[int(login_as)]
    return user


@app.before_request
def before_request():
    """
    Operations before request.
    """
    user = get_user()
    g.user = user


@app.route('/')
def index():
    """
    Index view for app
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
