from flask import Flask, render_template, request, redirect, url_for
from menu_configurations import menus
from handlers import Handlers
from service import Services
import datetime


app = Flask(__name__)


@app.route("/", methods=["get"])
def welcome():
    (
        zebra_crossing_violation,
        no_parking_violation,
        red_signal_violation,
        heavy_vehicle_violation,
    ) = Services().get_violations_count()
    return render_template(
        "index.html",
        menu=menus.dashboard_menus,
        violations_list=menus.violations,
        zebra_crossing_violation=zebra_crossing_violation,
        no_parking_violation=no_parking_violation,
        red_signal_violation=red_signal_violation,
        heavy_vehicle_violation=heavy_vehicle_violation,
        datetime=datetime.datetime.now(),
    )


@app.route("/admin/traffic/control", methods=["get"])
def traffic_control_system():
    info = "Page under construction"
    return render_template(
        "traffic_control_new.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/live", methods=["get"])
def live_camera_view():
    info = "Page under construction"
    return render_template(
        "live_traffic_view.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/redsignalcrossing", methods=["get"])
def red_signal_crossing():
    folder_location = "static/violations/red_signal"

    return render_template(
        "redsignal_crossing_new.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/heavy/schooltime", methods=["get"])
def truck_in_schooltime():
    return render_template(
        "trucks_schooltime_new.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/zebracrossing", methods=["get"])
def vehicles_in_zebra_cross():
    return render_template(
        "zebra_crossing_new.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/vehicles/noparking", methods=["get"])
def no_parking_violation():
    return render_template(
        "noparking_new.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/violation/pedestrian/crossing", methods=["get"])
def pedestrian_crossing_violation():
    return render_template(
        "pedestrian_crossing.html",
        menu=menus.dashboard_menus,
    )


@app.route("/admin/traffic/density", methods=["get"])
def traffic_density():
    (
        zebra_crossing_violation,
        no_parking_violation,
        red_signal_violation,
        heavy_vehicle_violation,
    ) = Services().get_violations_count()
    return render_template(
        "traffic_density_new.html",
        menu=menus.dashboard_menus,
        status=False,
        zebra_crossing_violation=zebra_crossing_violation,
        no_parking_violation=no_parking_violation,
        red_signal_violation=red_signal_violation,
        heavy_vehicle_violation=heavy_vehicle_violation,
    )


@app.route("/admin/violation/charged", methods=["get"])
def charged_violation():
    rows = Services().get_violations(None)

    return render_template(
        "charged_violations_new.html",
        menu=menus.dashboard_menus,
        rows=rows,
    )


@app.route("/extract_images1", methods=["get"])
def extract_images_camera1():
    status = Services().video_to_images_traffic1()
    return render_template(
        "live_camera.html",
        menu=menus.dashboard_menus,
        status=status,
    )


@app.route("/extract_images2", methods=["get"])
def extract_images_camera2():
    status = Services().video_to_images_traffic2()
    return render_template(
        "live_traffic_view.html",
        menu=menus.dashboard_menus,
        status=status,
    )


@app.route("/red_signal_violation_processing", methods=["post"])
def red_signal_violation_processing():
    image_path, filename = Handlers().handle_image_uploads()
    status = Services().track_violation(image_path, "RED_SIGNAL_CROSSING")
    return render_template(
        "redsignal_crossing_new.html",
        menu=menus.dashboard_menus,
        image_file=filename,
    )


@app.route("/vehicles_in_zebra_crossing_violation_processing", methods=["post"])
def vehicles_in_zebra_crossing_violation_processing():
    image_path, filename = Handlers().handle_image_uploads()

    status = Services().track_violation(image_path, "ZEBRA_CROSSING_VEHICLE")
    return render_template(
        "zebra_crossing_new.html",
        menu=menus.dashboard_menus,
        image_file=filename,
    )


@app.route("/no_parking_violation_processing", methods=["post"])
def no_parking_processing():
    image_path, filename = Handlers().handle_image_uploads()

    status = Services().track_violation(image_path, "NO_PARKING")
    return render_template(
        "noparking.html",
        menu=menus.dashboard_menus,
        image_file=filename,
    )


@app.route("/heavy_vehicles_violation", methods=["post"])
def heavy_vehicles_violation_processing():
    image_path, filename = Handlers().handle_image_uploads()

    status = Services().track_truck_in_school_hrs(
        image_path, "HEAVY_VEHICLES_VIOLATION"
    )
    return render_template(
        "trucks_schooltime.html",
        menu=menus.dashboard_menus,
        image_file=filename,
    )


@app.route("/traffic_density", methods=["post"])
def traffic_density_process():
    image_path, filename = Handlers().handle_image_uploads()
    vehicle_segregated_count = Services().get_vehicle_count_details(image_path, None)
    try:
        vehicle_segregated_count["truck"]
    except:
        vehicle_segregated_count["truck"] = 0
    try:
        vehicle_segregated_count["car"]
    except:
        vehicle_segregated_count["car"] = 0
    try:
        vehicle_segregated_count["motorbike"]
    except:
        vehicle_segregated_count["motorbike"] = 0
    try:
        vehicle_segregated_count["bus"]
    except:
        vehicle_segregated_count["bus"] = 0
    return render_template(
        "traffic_density_new.html",
        menu=menus.dashboard_menus,
        image_file=filename,
        vehicle_segregated_count=vehicle_segregated_count,
        datetime=datetime.datetime.now(),
        status=True,
    )


@app.route("/traffic_control", methods=["post"])
def traffic_control():
    (
        image_path_1,
        image_path_2,
        image_path_3,
        image_path_4,
    ) = Handlers().handle_multiple_image_uploads()
    junction1_data = Services().get_vehicle_count_details(image_path_1, None)
    junction2_data = Services().get_vehicle_count_details(image_path_2, None)
    junction3_data = Services().get_vehicle_count_details(image_path_3, None)
    junction4_data = Services().get_vehicle_count_details(image_path_4, None)

    (
        junction1_vehicle_count,
        junction2_vehicle_count,
        junction3_vehicle_count,
        junction4_vehicle_count,
    ) = Services().get_vehicle_count(
        junction1_data,
        junction2_data,
        junction3_data,
        junction4_data,
    )
    traffic_control_data = Services().control_traffic_light(
        junction1_vehicle_count,
        junction2_vehicle_count,
        junction3_vehicle_count,
        junction4_vehicle_count,
    )

    vehicle_segregated_count1 = Services().get_vehicle_count_details(image_path_1, None)
    try:
        vehicle_segregated_count1["truck"]
    except:
        vehicle_segregated_count1["truck"] = 0
    try:
        vehicle_segregated_count1["car"]
    except:
        vehicle_segregated_count1["car"] = 0
    try:
        vehicle_segregated_count1["motorbike"]
    except:
        vehicle_segregated_count1["motorbike"] = 0
    try:
        vehicle_segregated_count1["bus"]
    except:
        vehicle_segregated_count1["bus"] = 0

    vehicle_segregated_count2 = Services().get_vehicle_count_details(image_path_2, None)
    try:
        vehicle_segregated_count2["truck"]
    except:
        vehicle_segregated_count2["truck"] = 0
    try:
        vehicle_segregated_count2["car"]
    except:
        vehicle_segregated_count2["car"] = 0
    try:
        vehicle_segregated_count2["motorbike"]
    except:
        vehicle_segregated_count2["motorbike"] = 0
    try:
        vehicle_segregated_count2["bus"]
    except:
        vehicle_segregated_count2["bus"] = 0

    vehicle_segregated_count3 = Services().get_vehicle_count_details(image_path_1, None)
    try:
        vehicle_segregated_count3["truck"]
    except:
        vehicle_segregated_count3["truck"] = 0
    try:
        vehicle_segregated_count3["car"]
    except:
        vehicle_segregated_count3["car"] = 0
    try:
        vehicle_segregated_count3["motorbike"]
    except:
        vehicle_segregated_count3["motorbike"] = 0
    try:
        vehicle_segregated_count3["bus"]
    except:
        vehicle_segregated_count3["bus"] = 0

    vehicle_segregated_count4 = Services().get_vehicle_count_details(image_path_1, None)
    try:
        vehicle_segregated_count4["truck"]
    except:
        vehicle_segregated_count4["truck"] = 0
    try:
        vehicle_segregated_count4["car"]
    except:
        vehicle_segregated_count4["car"] = 0
    try:
        vehicle_segregated_count4["motorbike"]
    except:
        vehicle_segregated_count4["motorbike"] = 0
    try:
        vehicle_segregated_count4["bus"]
    except:
        vehicle_segregated_count4["bus"] = 0

    return render_template(
        "traffic_control_new.html",
        menu=menus.dashboard_menus,
        traffic_control_data=traffic_control_data,
        vehicle_segregated_count1=vehicle_segregated_count1,
        vehicle_segregated_count2=vehicle_segregated_count2,
        vehicle_segregated_count3=vehicle_segregated_count3,
        vehicle_segregated_count4=vehicle_segregated_count4,
        status=True,
        datetime=datetime.datetime.now(),
    )


@app.route("/view_violation_image", methods=["post"])
def view_violation_image():
    id = Handlers().handle_violation_id()
    filename = Services().select_violation(id)

    return render_template(
        "charged_violations_new.html",
        menu=menus.dashboard_menus,
        filename=filename,
    )


@app.route("/redirect_approval", methods=["post"])
def redirect_approval():
    return render_template(
        "validate_violations_new.html",
        menu=menus.dashboard_menus,
    )


@app.route("/validate_violations", methods=["post"])
def validate_violations():
    id = Handlers().handle_violation_id()
    Services().validate_violations(id)
    return render_template(
        "charged_violations_new.html",
        menu=menus.dashboard_menus,
    )


if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
