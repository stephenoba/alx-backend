#!/usr/bin/env python3
"""
Basic Flask app that creates a single / route.
"""
from flask import Flask, render_template
from flask import request
from flask_babel import Babel, _


def get_locale():
    """
    Get User's locale from AcceptLanguagesx header
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """
    Config for babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


home_title = _("Welcome to Holberton")
home_header = _("Hello World!")


@app.route('/')
def index():
    """
    Index view for app
    """
    return render_template('3-index.html', title=home_title, header=home_header)


if __name__ == '__main__':
    app.run(debug=True)
