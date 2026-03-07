# import methods and objects from flask
from flask import render_template, redirect, url_for, request, session, flash

from config.database import get_db

from app import app


# create the routes
@app.route('/', methods = ["GET", "POST"])
def index():
    """
    Handle the landing page and user login process.
    For GET request, this function renders the login page.
    For POST request, it attempts to authenticate the user:
        if the user is administrator render the administrator dashboard
        if the user is a employee render the employee dashboard
    """
    if request.method == "POST":
        username = request.form.get("user") # joseiungo
        password = request.form.get("password")
#jose@iungo.
        if username.find('@') != -1: # check if joseiungo
            # invoke a function to retrieve the user from the database ussing the email
        else:
            # invoke a function to retrieve the user from the database using the username
        
        # check if the user retrieve from the database  != None -> create the session

            # redirect by role
            # if the user is admin

        #if the user doesn't exist:
        #display a message
        flash("wrong credential. Try again!", "error")
        return redirect(url_for("index"))

    return render_template("index.html")

