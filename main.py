"""
MBTA stop locater application using Flask.
"""
from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import *

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/MBTA_Helper/', methods=['GET', 'POST'])
def MBTA_Helper():
    '''
    This first renders the input form webpage.
    Then takes the user's input from the text field and uses the functions present in
    mbta_helper.py to find the nearest stop name and distance.
    Finally, it renders the results template based on the presence of an error, or 
    the accurate result of a nearby stop. 
    '''
    if request.method == 'POST':
        location = request.form['location']
        stopname, distance = find_stop_near(location)
        if(distance == 'Inf miles away'):
            if stopname:
                return render_template('MBTA_Helper_result.html', location =location, stopname = stopname, distance = distance, error = "Don't panic. Your location could not be found or returned multiple results. Please try entering a different location. If you entered the name of a landmark, try adding 'Boston' at the end to specify the city.")
        else:
            distance = round(float(distance),2)
            if stopname:
                return render_template('MBTA_Helper_result.html', location =location, stopname = stopname, distance = distance, error = "")

    return render_template('MBTA_Helper_form.html')

if __name__ == '__main__':
    app.run()