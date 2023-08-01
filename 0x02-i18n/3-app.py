#!/usr/bin/env python3
"""
Basic Flask app that creates a single / route.
"""
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Index view for app
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
