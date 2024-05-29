#!/usr/bin/env python3
"""
basic Babel Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel, lazy_gettext


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def get_index() -> str:
    """
    gets index page
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the locale for a web page.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
