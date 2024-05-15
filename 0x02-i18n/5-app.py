#!/usr/bin/env python3
"""simple flask app outputs “Welcome to Holberton” as
page title (<title>) and “Hello world”
as header (<h1>)
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    if request.args.get('locale'):
        lanG = request.args.get('locale')
        if lanG in app.config['LANGUAGES']:
            return lanG
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """returns a user dictionary
    or None if the ID cannot be found
    or if login_as was not passed.
    """
    USERid = request.args.get('login_as', None)
    if USERid:
        return users.get(int(USERid))
    return None

@app.before_request
def before_request():
    """
    Function that it be executed before all other functions.
    because of the preceeding decorator
    """
    g.user = get_user()

@app.route('/', methods=['GET'], strict_slashes=False)
def home_route() -> str:
    """route to home page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
