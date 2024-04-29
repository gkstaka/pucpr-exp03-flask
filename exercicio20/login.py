from flask import Blueprint, Flask, render_template, request, redirect, url_for

login = Blueprint("login", __name__, template_folder="templates")

users = {
    "user1": "1234",
    "user2": "1234",
    "123": "123"
}


@login.route("/validate_user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        id = request.form["user"]
        password = request.form["password"]
        if id in users and users[id] == password:
            return render_template("home.html")
        else:
            return render_template("invalid_user.html")

    return render_template("login.html")


@login.route("/list_users")
def list_users():
    return render_template("list_users.html", dictionary=users, dict_type="Usuarios")


@login.route("/register_user")
def register_user():
    return render_template("register_user.html")


@login.route("/register_user_form", methods=["POST", "GET"])
def register_user_form():
    global users
    if request.method == "POST":
        id = request.form["user"]
        password = request.form["password"]
    else:
        id = request.args.get("user", None)
        password = request.args.get("password", None)
    users[id] = password
    return render_template("list_users.html", dictionary=users, dict_type="Usuarios")


@login.route("/remove_user")
def remove_user():
    return render_template("remove_user.html", dictionary=users)


@login.route("/del_user", methods=["GET", "POST"])
def del_user():
    global users
    if request.method == "POST":
        user = request.form["user"]
    else:
        user = request.args.get("user", None)
    users.pop(user)
    return render_template("list_users.html", dict_type="Usuarios", dictionary=users)
