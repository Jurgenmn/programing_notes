from flask import Flask
import flask
from flask.helpers import _PackageBoundObject
from werkzeug.exceptions import _EnvironContainer

app = Flask(__name__)


@app.route("/")  # Route (This is a server that always is listening)
def hello_world():  # Handler
    return "<p>Hello, World!</p>"


@app.route("/index.html")  # Route
def index():  # Handler
    return """
        <!DOCTYPE html>
        <html>
        <body>

        <h1>My First Heading</h1>
        <p>My first paragraph.</p>

        </body>
        </html>
        """


@app.route("/about.html")  # Route
def about():  # Handler
    return """
        <!DOCTYPE html>
        <html>
        <body>

        <h3>My My About Page</h3>
        <p>My first paragraph.</p>

        </body>
        </html>
        """


@app.route("/about.html/me/and/my/family")  # Route
def aboutme():  # Handler
    return """
        <!DOCTYPE html>
        <html>
        <body>

        <h3>My Family Page</h3>
        <p>My first paragraph.</p>

        </body>
        </html>
        """


app.run("localhost", 3000, debug=True)


make a new directory
virtual _Env
instal flask
create 2 routs
3 routs
1 its gonna return html File / me.html(should be your prtofolio)
2 / user/Jamal its gonna return HELLO JAMAL
generate requrements.txt
