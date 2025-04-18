import cv2
import collections
import numpy as np
from Engine.VisionLogic.tracker import *

# Initialize Tracker
tracker = EuclideanDistTracker()
violation_tracker = ViolationTracker()

# Initialize the videocapture object
input_size = 320

# Detection confidence threshold
confThreshold = 0.2
nmsThreshold = 0.2

font_color = (0, 0, 255)
font_size = 0.5
font_thickness = 2

# Middle cross line position
middle_line_position = 225
up_line_position = middle_line_position - 15
down_line_position = middle_line_position + 15


# Store Coco Names in a list
classesFile = "Engine/VisionLogic/coco.names"
classNames = open(classesFile).read().strip().split("\n")
# print(classNames)
# print(len(classNames))

# class index for our required detection classes
required_class_index = [2, 3, 5, 7]

detected_classNames = []

## Model Files
modelConfiguration = "Engine/VisionLogic/yolov3-320.cfg"
modelWeigheights = "Engine/VisionLogic/yolov3-320.weights"

# configure the network model
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigheights)

# Configure the network backend

# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Define random colour for each class
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classNames), 3), dtype="uint8")


# Function for finding the center of a rectangle
def find_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


# Function for count vehicle
def count_vehicle(box_id, img, image_path, functionality):

    x, y, w, h, id, index = box_id
    # Find the center of the rectangle for detection
    # print(index)
    center = find_center(x, y, w, h)
    # print(center)

    # Draw circle in the middle of the rectangle
    if functionality == "RED_SIGNAL_CROSSING":
        violation_tracker.red_signal_crossing(center, img, image_path)
    elif functionality == "HEAVY_VEHICLES_VIOLATION":
        violation_tracker.truck_in_schooltime(img, image_path)
    elif functionality == "NO_PARKING":
        violation_tracker.no_parking(center, img, image_path)
    elif functionality == "ZEBRA_CROSSING_VEHICLE":
        violation_tracker.vehicle_zebra_crossing(center, img, image_path)
    else:
        cv2.circle(img, center, 2, (0, 0, 255), -1)

    # end here
    # print(up_list, down_list)


# Function for finding the detected objects from the network output
def postProcess(outputs, img, image_path, functionality):
    global detected_classNames
    height, width = img.shape[:2]
    boxes = []
    classIds = []
    confidence_scores = []
    detection = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if classId in required_class_index:
                if confidence > confThreshold:
                    # print(classId)
                    w, h = int(det[2] * width), int(det[3] * height)
                    x, y = int((det[0] * width) - w / 2), int((det[1] * height) - h / 2)
                    boxes.append([x, y, w, h])
                    classIds.append(classId)
                    confidence_scores.append(float(confidence))

    # Apply Non-Max Suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidence_scores, confThreshold, nmsThreshold)
    # print(classIds)
    for i in indices.flatten():
        x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]
        # print(x,y,w,h)

        color = [int(c) for c in colors[classIds[i]]]
        name = classNames[classIds[i]]
        detected_classNames.append(name)
        # Draw classname and confidence score
        cv2.putText(
            img,
            f"{name.upper()} {int(confidence_scores[i]*100)}%",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1,
        )

        # Draw bounding rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
        detection.append([x, y, w, h, required_class_index.index(classIds[i])])

    # Update the tracker for each object
    boxes_ids = tracker.update(detection)
    for box_id in boxes_ids:
        count_vehicle(box_id, img, image_path, functionality)


def process_image(image_path, functionality):
    img = cv2.imread(image_path)
    blob = cv2.dnn.blobFromImage(
        img, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False
    )

    # Set the input of the network
    net.setInput(blob)
    layersNames = net.getLayerNames()
    outputNames = [(layersNames[i - 1]) for i in net.getUnconnectedOutLayers()]
    # Feed data to the network
    outputs = net.forward(outputNames)

    # Find the objects from the network output
    postProcess(outputs, img, image_path, functionality)

    # count the frequency of detected classes

    frequency = collections.Counter(detected_classNames)
    detected_classNames.clear()
    # print(frequency)

    # Draw counting texts in the frame

    # cv2.imshow("Processed Image", img)

    # cv2.waitKey(0)
    return dict(frequency)
