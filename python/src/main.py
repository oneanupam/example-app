"""
This module uses flask web framework to deploy a sample web application.
"""

from flask import Flask, redirect, url_for, render_template, request, session
from .validlogin import valid_login

app = Flask(__name__)

@app.route("/")
def index():
    """ Brief summary of what the function does. """
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """ Brief summary of what the function does. """
    if request.method == "POST":
        if valid_login(request.form["t1"], request.form["t2"]):
            session["username"] = request.form["t1"]
            return redirect(url_for("home"))
        else:
            error_message = "Incorrect Username or Password."
            return render_template("login.html", error = error_message)
    return render_template("login.html")

@app.route("/home")
def home():
    """ Brief summary of what the function does. """
    return render_template("home.html", user = session["username"])

@app.route("/logout")
def logout():
    """ Brief summary of what the function does. """
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/maintenance")
def maintenance():
    """ Brief summary of what the function does. """
    return "Sorry, we are under maintenance. Try to login with same username and password."
