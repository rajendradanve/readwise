import os
import datetime
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

    books = mongo.db.books.find()
    return render_template("index.html", books=books)


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

        existing_book = mongo.db.books.find_one(
            {"book_name": request.form.get("book_name").strip()})
        
        if existing_book:
            flash("Book already exist")
        else:
            book_name = request.form.get("book_name").strip().title()
            date = datetime.datetime.now().date()
            today_date = date.strftime("%x")
            current_time = date.strftime("%H:%M")

            add_book = {
                "book_name": book_name,
                "book_author": request.form.get("book_author"),
                "book_language": request.form.get("book_language"),
                "book_category": request.form.get("book_category"),
                "book_age_group": request.form.get("book_age_group"),
                "book_summary": request.form.get("book_summary"),
                "book_shopping-link": request.form.get("book_shopping-link"),
                "book_image_url": request.form.get("book_image_url"),
                "book_added_by_user": session["username"],
                "book_added_date": today_date,
                "book_added_time": current_time
            }

            mongo.db.books.insert_one(add_book)
            flash("Book Data Added Successfully")
            return redirect(url_for("add_book"))

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
    # check is admin is log in to show profile page.
    if session["username"] != "admin":
        return redirect(url_for("index"))

    return render_template("profile.html", username=username)


@app.route("/book/<book_id>")
def book_detail(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book.html", book=book)


@app.route("/add_category/", methods=["GET", "POST"])
def add_category():

    if request.method == "POST":
        new_category = request.form.get("new_category")
        new_category = new_category.strip().title().replace(" And ", " & ")
        # Check if category already exist in the list
        existing_category = mongo.db.categories.find_one(
                {"category": new_category})
        
        if existing_category:
            flash("Category Already Exists")
        else:
            mongo.db.categories.insert_one({"category": new_category})
            flash("Category Added Successfully")
            return redirect(url_for("add_category"))

    return render_template("add_category.html")


@app.route("/add_language/", methods=["GET", "POST"])
def add_language():

    if request.method == "POST":
        new_language = request.form.get("new_language")
        new_language = new_language.strip().title()
        # Check if category already exist in the list
        existing_language = mongo.db.languages.find_one(
                {"language": new_language})
        
        if existing_language:
            flash("Language Already Exists")
        else:
            mongo.db.languages.insert_one({"language": new_language})
            flash("Language Added Successfully")
            return redirect(url_for("add_language"))
    return render_template("add_language.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.tasks.find({"$text": {"$search":query}}))
    return render_template("index.html", books=books)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port = int(os.environ.get("PORT")),
            debug = True)