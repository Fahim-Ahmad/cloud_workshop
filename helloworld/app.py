"""
Sample flask application with index.html and welcome.html pages

index.html: simple html file with "Hello World!" text, image (img/MIT.png) 
and a form field with "Name:" field, and "Submit" button, sending a POST request to welcome.html

welcome.html: simple html file with "Hello <username>!" text and image (img/MIT.png), 
response from POST request with Name data.

String with Name is processed with str.title()

All code is simple flask routines, providing required functionality 

Author: tvsirius
Date: 2024-04-29
"""

import flask

app = flask.Flask(__name__, static_folder='img')

@app.route('/')
def index():
    """Render the index.html page.

    Returns:
        str: Rendered HTML content of the index.html page.
    """
    return flask.render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    """Render the welcome.html page with the processed username from the form.

    Returns:
        str: Rendered HTML content of the welcome.html page with the processed username.
    """
    # Here we take the string from the input filed in form of the HTML file
    # and apply str.title() method to it
    name = flask.request.form['Username'].title()
    
    # this method renders the HTML template, using our data
    return flask.render_template('welcome.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)
