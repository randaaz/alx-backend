#!/usr/bin/env python3
'''
    Basic Flask app with a single route.
'''

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Route for the home page.
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
