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
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exist")
        elif request.form.get("user_password") != request.form.get(
                "user_password_confirm"):
            flash("Password doesn't match")
        else:
            register = {
                "username": request.form.get("username"),
                "user_password": generate_password_hash(
                    request.form.get("user_password"))
                }

            mongo.db.users.insert_one(register)

            session["username"] = request.form.get("username")
            flash(f"Welcome {session['username']}")
            return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
       
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["user_password"], request.form.get(
                        "user_password")):
                session["username"] = request.form.get("username").lower()
                return redirect(url_for(
                    "index", username=session["username"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        add_book = {
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author")
        }

    languages = mongo.db.languages.find().sort("language", 1)
    categories = mongo.db.categories.find().sort("category", 1)
    age_groups = mongo.db.age_groups.find().sort("age_group", 1)
    return render_template(
            "add_book.html", languages=languages, categories=categories,
            age_groups=age_groups)



@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("username")
    return redirect(url_for("index"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from
    username = mongo.db.users.find_one(
        {"username": session["username"]})["username"]
    
    if session["username"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("index"))



@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.tasks.find({"$text":{"$search":query}}))
    return render_template("index.html", books=books)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port =int(os.environ.get("PORT")),
            debug =True)