#!/usr/bin/env python3
"""simple flask app outputs “Welcome to Holberton” as
page title (<title>) and “Hello world”
as header (<h1>)
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


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


def get_locale() -> str:
    """get_locale function"""
    # Locale from URL parameters
    if request.args.get('locale'):
        lanG = request.args.get('locale')
        if lanG in app.config['LANGUAGES']:
            return lanG

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Locale from request header
    header_locale = request.accept_languages.best_match(
            app.config['LANGUAGES']
    )
    if header_locale:
        return header_locale
    # Default locale
    return request.accept_languages.best_match(
            app.config['LANGUAGES']
        )


babel.init_app(app, locale_selector=get_locale)


def get_timezone() -> str:
    """get_timezone function"""
    # Timezone from URL parameters
    if request.args.get('timezone'):
        tz = request.args.get('timezone')
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass

    # Timezone from user settings
    if g.user and g.user.get('timezone'):
        tz = g.user.get('timezone')
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass

    # Default timezone
    return app.config.get('BABEL_DEFAULT_TIMEZONE', 'UTC')

babel.init_app(app, timezone_selector=get_timezone)


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


@app.route('/', strict_slashes=False)
def home_route() -> str:
    """route to home page"""
	# get the user's timezone
    tz = get_timezone()
    if tz is None:
        tz = 'UTC'

    # Get the current time in the user's timezone
    now = datetime.now(pytz.timezone(tz))

    # Format the time
    time_str = now.strftime('%b %d, %Y, %I:%M:%S %p')

    if g.user is None:
        return render_template('index.html', time=time_str)  # "Please log in to view your profile."
    else:
        return render_template('index.html', user=g.user, time=time_str)
    # return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
