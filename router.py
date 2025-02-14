from flask import Flask, render_template, request, redirect, url_for
from menu_configurations import menus


app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def welcome():
    return render_template(
        "dashboard.html",
        dashboard=menus.dashboard_menus,
    )

if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
