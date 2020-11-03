from flask import render_template, request, Blueprint, redirect, url_for, session, flash
from models.user import User, UserErrors

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            User.register_user(email, password)
            session["email"] = email
            return render_template("users/menu.html")
        except UserErrors.UserError as e:
            flash(e.message, "danger")
            return render_template("users/register.html")

    return render_template("users/register.html")


@user_blueprint.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            if User.is_login_valid(email, password):
                session["email"] = email
                return render_template("users/menu.html")
        except UserErrors.UserError as e:
            flash(e.message, "danger")
            return render_template("users/login.html")

    return render_template("users/login.html")


@user_blueprint.route("/logout")
def logout_user():
    session["email"] = None
    return redirect(url_for(".login_user"))
