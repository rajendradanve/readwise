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
@app.route("/index", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        # check if username already exist in db
        existing_user = mongo.db.users.find_one(
            {"user_email": request.form.get("user_email").lower()})

        if existing_user:
            flash("Username already exist")
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

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port =int(os.environ.get("PORT")),
        debug =True)