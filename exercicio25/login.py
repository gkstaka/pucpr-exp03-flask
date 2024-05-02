from flask import Blueprint, Flask, render_template, request, redirect, url_for, current_app, flash

login = Blueprint("login", __name__, template_folder="templates")

users = {
    "user1": {
        "password": "1234",
        "privilege": "admin"
    },
    "user2": {
        "password": "1234",
        "privilege": "user"
    },

    "123": {
        "password": "1234",
        "privilege": "user"
    }
}


@login.route("/validate_user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        id = request.form["user"]
        password = request.form["password"]
        if id in users and users[id]["password"] == password:
            current_app.config["privilege"] = users[id]["privilege"]
            return render_template("home.html", privilege=current_app.config["privilege"])
        else:
            return render_template("invalid_user.html")

    return render_template("login.html")


@login.route("/list_users")
def list_users():
    return render_template("list_users.html", dictionary=users, dict_type="Usuarios" , privilege=current_app.config["privilege"])


@login.route("/register_user")
def register_user():
    return render_template("register_user.html", privilege=current_app.config["privilege"])


@login.route("add_user", methods=["POST", "GET"])
def add_user():
    global users
    if request.method == "POST":
        id = request.form["user"]
        password = request.form["password"]
    else:
        id = request.args.get("user", None)
        password = request.args.get("password", None)
    if id not in users.keys():
        users[id] = {
            "password": password,
            "privilege": "user"
        }
    else:
        flash("Usuario ja existente")
                
    return render_template("list_users.html", dictionary=users, dict_type="Usuarios", privilege=current_app.config["privilege"])

@login.route("/edit_username")
def edit_username():
    return render_template ("edit_username.html", privilege=current_app.config["privilege"])

@login.route("/edit_username_form", methods=["POST"])
def edit_username_form():
    if request.method == "POST":
        old_id = request.args.get('user')
        new_id = request.form.get('user')
        if new_id not in users.keys():
            info = users.pop(old_id)
            users[new_id] = info
    return redirect("list_users", privilege=current_app.config["privilege"])

@login.route("/edit_password")
def edit_password():
    return render_template ("edit_password.html", privilege=current_app.config["privilege"])

@login.route("/edit_password_form", methods=["POST"])
def edit_password_form():
    if request.method == "POST":
        id = request.args.get('user')
        password = request.form.get('password')
        users[id]["password"]= password
    return redirect("list_users", privilege=current_app.config["privilege"])

@login.route("/remove_user")
def remove_user():
    return render_template("remove_user.html", dictionary=users, privilege=current_app.config["privilege"])


@login.route("/del_user", methods=["GET", "POST"])
def del_user():
    global users
    if request.method == "POST":
        user = request.form["user"]
    else:
        user = request.args.get("user", None)
    users.pop(user)
    return render_template("list_users.html", dict_type="Usuarios", dictionary=users, privilege=current_app.config["privilege"])

@login.route('/logout')
def logout():
    return render_template('login.html')