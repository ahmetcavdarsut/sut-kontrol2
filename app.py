
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html", error="Hatalı giriş!")
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    return "<h1>SUT kontrolüne hoş geldin.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
