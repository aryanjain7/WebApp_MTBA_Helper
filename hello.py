"""
Simple "Hello, World" application using Flask
"""
from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import *

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/MBTA_Helper/', methods=['GET', 'POST'])
def MBTA_Helper():
    if request.method == 'POST':
        location = request.form['location']
        stopname, distance = find_stop_near(location)
        if stopname:
            return render_template('MBTA_Helper_result.html', location =location, stopname = stopname, distance = distance)

    return render_template('MBTA_Helper_form.html')

if __name__ == '__main__':
    app.run()