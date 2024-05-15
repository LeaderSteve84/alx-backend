#!/usr/bin/env python3
"""simple flask app outputs “Welcome to Holberton” as
page title (<title>) and “Hello world”
as header (<h1>)
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class for the configuration for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get_locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home_route() -> str:
    """route to home page"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
