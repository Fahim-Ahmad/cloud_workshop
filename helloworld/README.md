# [Helloworld Application](helloworld)

![application](../imgs/app_screenshot.png)

Simple web application on Flask with "Hello world!" and a form input field for a username. The "Submit" button sends a POST request with the name, resulting in a "Hello \<Username\>!" response. The name is modified using the `str.title()` method, capitalizing the name, for basic functionality. Includes a Python file, an HTML template, and an image in a subfolder. 

## Running 

You will need to install Flask:

```bash
pip install flask
```

Run the `app.py` locally using this command (be sure to be in the application folder):

```bash
flask run
```

Alternatively, you may just run it with the RUN command in your IDE. Running will result in something like this:

```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 498-754-683
```

This means you just started a local Flask server, which is constantly running and will process all requests to `http://127.0.0.1:5000`. `127.0.0.1` by network standard relates to your local PC and can also be named as `localhost`. 

## Functionality

With the Flask server running with the application, when you enter this address into your local browser: `http://127.0.0.1:5000` or `http://localhost:5000` the running Flask server will process this request, by running the specified function in the `app.py`:

```python
# This decorator tells Flask that the function index_page() will process requests to '/'
@app.route('/')
def index_page():
    """Render the index.html page.
    This function is called when Flask receives a GET request to '/' endpoint

    Returns:
        str: Rendered HTML content of the index.html page.
    """
    return flask.render_template('index.html', processed_data1='')
```

`http://localhost:5000` corresponds to '/', so the application will run and respond to your browser with the rendered `index.html` file. 

Inside `index.html`, there is a form with a field for input:

```html
<form action="/computation" method="post">
    <label for="input1">Input field (your name):</label>
    <input type="text" id="input1" name="input_data1" required>
    <input type="submit" value="Submit">
</form>
```

Here `<input type="submit" value="Submit">` is a submit button, and `<form action="/computation" method="post">` is the name of the entrypoint, and the type of request that the form will send. Line `<input type="text" id="name" name="input_data1" required>` contains the type("text") and name("input_data1") of the data that will be sent with the request. So pressing the `Submit` button will send a new POST request to the endpoint `http://127.0.0.1:5000/computation`, along with the data you entered into the "input_data1" field.

When Flask receives the POST request to `http://127.0.0.1:5000/computation`, it will run this function:

```python
# This decorator tells Flask that the function computation_page() will process POST requests to '/computation'
@app.route('/computation', methods=['POST'])
def computation_page():
    """Render the computation HTML page with the processed input from the form.
    This function is called when Flask receives a POST request to '/computation' endpoint  
    with this function will be able to get the data of the request, including the inputs of the form that sends this request 
```

This function will take the data from the form with the command `input_data1 = flask.request.form['input_data1']`, process it with the `my_basic_computation` function, and render HTML that will be sent as a response to your browser.

Note: This application uses only one HTML template (`index.html`), both for GET and POST responses, for simplicity. In the GET request (first time you open the page), it just renders `index.html` with `processed_data1=''`.

## Modifying

The `app.py` contains all needed comments to get the idea of how this web application works. You can make modifications to the `my_basic_computation` function. You can add more inputs to the HTML's form, add the needed code to pass this data to `my_basic_computation`, and modify the HTML for the correct names of input fields and processed data output.```
```