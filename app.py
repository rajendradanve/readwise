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

# Dict for multiple admin users
ADMIN_USER_NAMES = ['admin', 'admin1']


# Check if user is logged in
def is_logged_in():

    if session and session.get("username"):
        return True
    return False


# Check if logged in user is admin
def is_admin():
    if session and session["username"] in ADMIN_USER_NAMES:
        return True
    return False


# Main index page to show featured books
@app.route("/")
@app.route("/home")
def home():
    featured_books = list(mongo.db.books.find({"is_featured": True}))
    return render_template(
        "home.html", books_list=featured_books,
        is_user_logged=is_logged_in())


# Showing all books
@app.route("/books/all")
def all_books():
    books = list(mongo.db.books.find())
    return render_template("all_books.html", books_list=books,
                           is_user_logged=is_logged_in())


# Register new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if is_logged_in():
        return redirect(url_for("home"))

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
            return redirect(url_for("home"))

    return render_template("register.html")


# Sign in new user
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():

    if is_logged_in():
        return redirect(url_for("home"))

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
                    "home", username=session["username"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


# Add new book by logged in user.
@app.route("/book/add", methods=["GET", "POST"])
def add_book():

    if not is_logged_in():
        return redirect(url_for("home"))

    if request.method == "POST":

        existing_book = mongo.db.books.find_one(
            {"book_name": request.form.get("book_name").strip()})

        if existing_book:
            flash("Book already exist")
        else:
            book_name = request.form.get("book_name").strip().title()
            is_featured = True if request.form.get("is_featured") else False

            add_book = {
                "name": book_name,
                "author": request.form.get("book_author"),
                "language": request.form.get("book_language"),
                "category": request.form.get("book_category"),
                "age_group": request.form.get("book_age_group"),
                "summary": request.form.get("book_summary"),
                "shopping_link": request.form.get("book_shopping_link"),
                "image_url": request.form.get("book_image_url"),
                "added_by_user": session["username"],
                "is_featured":  is_featured,
                "added_timestamp": datetime.datetime.now()
            }

            mongo.db.books.insert_one(add_book)
            flash("Book Data Added Successfully")
            return redirect(url_for("add_book"))

    languages = mongo.db.languages.find().sort("language", 1)
    categories = mongo.db.categories.find().sort("category", 1)
    age_groups = mongo.db.age_groups.find().sort("age_group", 1)
    return render_template(
            "add_book.html", languages=languages, categories=categories,
            age_groups=age_groups, is_admin=is_admin(),
            is_user_logged=is_logged_in())


# Sign out user
@app.route("/sign_out")
def sign_out():

    if not is_logged_in():
        return redirect(url_for("home"))

    # remove user from session cookies
    flash("You have been logged out")
    session.pop("username")
    return redirect(url_for("home"))


# Showing profile
@app.route("/profile")
def profile():
    # check is user is log in to show profile page.
    if not is_logged_in():
        return redirect(url_for("home"))

    if is_admin():
        books = list(mongo.db.books.find())
    else:
        books = list(mongo.db.books.find(
                                    {"added_by_user": session["username"]}))

    return render_template("profile.html", is_user_logged=is_logged_in(),
                           is_admin=is_admin(), books_list=books)


# Showing books details.
# Showing all comments related to book
@app.route("/book/<book_id>/view")
def book_detail(book_id):

    try:
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        if not book:
            return redirect(url_for("home"))

        comments = mongo.db.comments.find(
               {"book_id": book_id})

        is_already_commented = False

        if is_logged_in():
            is_already_commented = mongo.db.comments.find_one(
                {"username": session["username"],
                 "book_id": book_id})

        return render_template("book.html", book=book,
                               is_user_logged=is_logged_in(),
                               is_already_commented=is_already_commented,
                               comments=comments, is_admin=is_admin())

    except:
        return redirect(url_for("home"))



# Book review function and function to calculate avg review
@app.route("/book/<book_id>/review", methods=["GET", "POST"])
def book_review(book_id):
    if not is_logged_in():
        return redirect(url_for("book_detail", book_id=book_id))

    if request.method == "POST":

        try:
            book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

            if not book:
                return redirect(url_for("home"))

            star_rating = 0

            if request.form.get("star_rating"):
                star_rating = int(request.form.get("star_rating"))

            comment = {
                "username": session["username"],
                "book_id": book_id,
                "review_text": request.form.get("review_text"),
                "star_value": star_rating,
                "time_stamp": datetime.datetime.now()
            }

            mongo.db.comments.insert_one(comment)
            # Calculating avg_review after new comments added.
            # Adding / updating avg_review for the books collection

            avg_result = [
                {"$match": {"book_id": book_id}},
                {"$group": {"_id": "$book_id",
                            "avg": {"$avg": "$star_value"}}}
            ]

            avg_review_list = list(mongo.db.comments.aggregate(avg_result))

            avg_review = avg_review_list[0]["avg"]

            mongo.db.books.update_one({"_id": ObjectId(book_id)},
                                      {"$set": {"avg_review": avg_review}})
            flash("Review Added Successfully")
            return redirect(url_for("book_detail", book_id=book_id))

        except:
            return redirect(url_for("home"))


# Add category
@app.route("/category/add", methods=["GET", "POST"])
def add_category():

    if not is_admin():
        return redirect(url_for("home"))

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

    return render_template("add_category.html", is_user_logged=is_logged_in(),
                           is_admin=is_admin())


# Add language
@app.route("/language/add", methods=["GET", "POST"])
def add_language():

    if not is_admin():
        return redirect(url_for("home"))

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
    return render_template("add_language.html", is_user_logged=is_logged_in(),
                           is_admin=is_admin())


# Delete category
@app.route("/category/delete", methods=["GET", "POST"])
def delete_category():

    if not is_admin():
        return redirect(url_for("home"))

    if request.method == "POST":
        mongo.db.categories.remove({"_id": ObjectId(request.form.get(
                                    "cateogry-to-delete"))})
        flash("Category Deleted Successfully")
        return redirect(url_for("delete_category"))

    categories = list(mongo.db.categories.find().sort("category", 1))
    return render_template("delete_category.html", categories=categories,
                           is_user_logged=is_logged_in(),
                           is_admin=is_admin())


# Delete language
@app.route("/language/delete", methods=["GET", "POST"])
def delete_language():

    if not is_admin():
        return redirect(url_for("home"))

    if request.method == "POST":
        mongo.db.languages.remove({"_id": ObjectId(request.form.get(
                                    "language-to-delete"))})
        flash("Language Deleted Successfully")
        return redirect(url_for("delete_language"))

    languages = mongo.db.languages.find().sort("language", 1)
    return render_template("delete_language.html", languages=languages,
                           is_user_logged=is_logged_in(),
                           is_admin=is_admin())


# Edit selected book
@app.route("/book/<book_id>/edit", methods=["GET", "POST"])
def edit_book_id(book_id):

    if not is_logged_in():
        return redirect(url_for("home"))

    if request.method == "POST":

        book_name = request.form.get("book_name").strip().title()
        is_featured = True if request.form.get("is_featured") else False

        update_book = {
            "name": book_name,
            "author": request.form.get("book_author"),
            "language": request.form.get("book_language"),
            "category": request.form.get("book_category"),
            "age_group": request.form.get("book_age_group"),
            "summary": request.form.get("book_summary"),
            "shopping_link": request.form.get("book_shopping_link"),
            "image_url": request.form.get("book_image_url"),
            "added_by_user": session["username"],
            "updated_timestamp": datetime.datetime.now(),
            "is_featured":  is_featured
        }

        mongo.db.books.update_one({"_id": ObjectId(book_id)},
                                  {"$set": update_book})
        flash("Book Updated Successfully")

        return redirect(url_for('book_detail', book_id=book_id))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    languages = mongo.db.languages.find().sort("language", 1)
    categories = mongo.db.categories.find().sort("category", 1)
    age_groups = mongo.db.age_groups.find().sort("age_group", 1)
    return render_template(
            "edit_book_id.html", book=book, languages=languages,
            categories=categories, age_groups=age_groups,
            is_user_logged=is_logged_in(), is_admin=is_admin())


# Function to delete Book
@app.route("/delete/book/<book_id>")
def delete_book(book_id):

    # check is user is log in to show profile page.
    if not is_logged_in():
        return redirect(url_for("home"))

    try:
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

        if not book:
            return redirect(url_for("home"))

        mongo.db.books.remove({"_id": ObjectId(book_id)})
        flash("Book Deleted Successfully")
        return redirect(url_for("profile"))

    except:
        flash("Error To Delete Book. Try Again.")
        return redirect(url_for("profile"))


# Search book
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))

    return render_template("all_books.html", books=books,
                           is_user_logged=is_logged_in())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
