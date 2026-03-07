# import methods and objects from flask
from flask import render_template, redirect, url_for, request, session, flash

from config.database import get_db
from models import DatabaseOperations

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
        username_email = request.form.get("user") # joseiungo
        password = request.form.get("password")
#jose@iungo.
        if username_email.find('@') != -1: # check if joseiungo
            # invoke a function to retrieve the user from the database ussing the email
            user = DatabaseOperations.get_user_by_username(username_email, password)
        else:
            # invoke a function to retrieve the user from the database using the username
            user = DatabaseOperations.get_user_by_username(username_email, password)
        # check if the user retrieve from the database  != None -> create the session
        if user is not None:
            # redirect by role
            session["user_id"] = user[0]
            session["user_name"] = user[1]
            session["is_admin"] = user[2]
            
            #redirect by role
            # if the user is admin
            if session["is_admin"]:
                return redirect("/admin_dashboard")
            
            return redirect("/user_dashboard")

        #if the user doesn't exist:
        #display a message
        flash("wrong credential. Try again!", "error")
        return redirect(url_for("index"))

    return render_template("index.html")

