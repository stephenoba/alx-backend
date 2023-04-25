#!/usr/bin/env python3
"""
Basic Flask app that creates a single / route.
"""
import pytz
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

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    1 Find timezone parameter in URL parameters
    2 Find time zone from user settings
    3 Default to UTC
    """
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tz = pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            tz = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tz = pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


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
