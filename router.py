from flask import Flask, render_template, request, redirect, url_for
from menu_configurations import menus
from service import Services


app = Flask(__name__)


@app.route("/", methods=["get"])
def welcome():
    return render_template(
        "dashboard.html",
        menu=menus.dashboard_menus,
        violations_list=menus.violations,
    )


@app.route("/admin/traffic/control", methods=["get"])
def traffic_control_system():
    info = "Page under construction"
    return render_template(
        "traffic_control.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/live", methods=["get"])
def live_camera_view():
    info = "Page under construction"
    return render_template(
        "live_camera.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/redsignalcrossing", methods=["get"])
def red_signal_crossing():
    folder_location = "static/violations/red_signal"

    return render_template(
        "redsignal_crossing.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/heavy/schooltime", methods=["get"])
def truck_in_schooltime():
    return render_template(
        "trucks_schooltime.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/zebracrossing", methods=["get"])
def vehicles_in_zebra_cross():
    return render_template(
        "zebra_crossing.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/noparking", methods=["get"])
def no_parking_violation():
    return render_template(
        "noparking.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/pedestrian/crossing", methods=["get"])
def pedestrian_crossing_violation():
    return render_template(
        "pedestrian_crossing.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/traffic/peakhours", methods=["get"])
def peak_hours():
    return render_template(
        "peak.html.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/charged", methods=["get"])
def charged_violation():
    return render_template(
        "charged_violations.html",
        menu=menus.dashboard_menus,
    )


if __name__ == "__main__":
    app.run("192.168.1.5", 5000, debug=True)
