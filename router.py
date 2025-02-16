from flask import Flask, render_template, request, redirect, url_for
from menu_configurations import menus
from models.camera_model import CameraPath


app = Flask(__name__)


@app.route("/", methods=["get"])
def welcome():
    return render_template(
        "dashboard.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/traffic/control", methods=["get"])
def traffic_control_system():
    info = "Page under construction"
    return render_template(
        "traffic_control.html",
        menu=menus.dashboard_menus,
    )


@app.route("/test", methods=["post"])
def get_traffic_density():
    return "This page under construction"


if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
