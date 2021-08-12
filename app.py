import os
from flask import (
    Flask, flash, render_template,  
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # check if username already exist in db
        existing_user = mongo.db.users.find_one(
            {"user_email": request.form.get("user_email").lower()})

        if existing_user:
            flash("Username already exist")
        elif ' ' in request.form.get('user_name')== False:
            flash("Enter Full Name")
        elif request.form.get("user_password") != request.form.get(
                "user_password_confirm"):
            flash("Password doesn't match")
        else:
            register = {
                "user_name": request.form.get("user_name"),
                "user_email": request.form.get("user_email").lower(),
                "user_password": generate_password_hash(
                    request.form.get("user_password"))
                }

            mongo.db.users.insert_one(register)

            session["user"] = request.form.get("user_email")
            session["user_name"] = request.form.get("user_name")
            flash(f"Welcome {session['user_name']}")
            return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():

    return render_template("sign_in.html")


@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/profile/<user_name>", methods=["GET", "POST"])
def profile(user_email):
    # grab the session user's username from
    user_email = mongo.db.users.find_one(
        {"user_email": session["user_email"]})["user_email"]
    user_name = mongo.db.users.find_one(
        {"user_name": session["user_email"]})["user_name"]
    
    if session["user_email"]:
        return render_template("profile.html", user_name=user_email)

    return redirect(url_for("index"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text":{"$search":query}}))
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port =int(os.environ.get("PORT")),
            debug =True)