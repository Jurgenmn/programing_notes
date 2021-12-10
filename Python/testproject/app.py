from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def time():
    time = datetime.now()
    # return str(time.year) + "/" + str(time.month) + "/" + str(time.day) + " " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
    return time.ctime()


@app.route("/how.html")
def how():
    handler = open("how.html", "r")
    return handler.read()


@app.route("/docs/about.txt")
def day():
    handler = open("docs/about.txt", "r")
    return handler.read()


@app.route("/user/<int:user_id>")
def return_user(user_id):
    print("The user id is " + str(user_id))
    return "User id is " + str(user_id)


app.run("localhost", 3000, debug=True)
