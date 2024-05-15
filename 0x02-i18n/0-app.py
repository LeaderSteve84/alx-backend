#!/usr/bin/env python3
"""simple flask app outputs “Welcome to Holberton” as
page title (<title>) and “Hello world”
as header (<h1>)
"""

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home_route() -> str:
    """route to home page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
