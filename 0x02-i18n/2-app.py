#!/usr/bin/env python3
"""Simple Flask app with Babel setup for internationalization.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration class for Flask-Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best matching language for localization.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Renders the index template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
