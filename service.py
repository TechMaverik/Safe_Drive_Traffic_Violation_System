import os
import cv2
from datetime import datetime
from Engine.VisionLogic import logic


class Services:

    def __init__(self):

        self.time = datetime.now()
        self.today_8am = datetime(2025, 3, 1, 8, 0)
        self.today_5pm = datetime(2026, 3, 22, 15, 50)

    def video_to_images_traffic1(self):

        video_path = "static\Traffic.mp4"
        output_folder = "ExtractedImageDataset"
        if not os.path.exists(str(output_folder)):
            os.makedirs(str(output_folder))

        vidcap = cv2.VideoCapture(str(video_path))

        if not vidcap.isOpened():
            print("Error opening video file.")
            return

        count = 0

        while True:

            success, frame = vidcap.read()

            if not success:
                break

            filename = os.path.join(str(output_folder), f"traffic_1_{count}.jpg")
            cv2.imwrite(filename, frame)

            count += 1

        vidcap.release()
        return True

    def video_to_images_traffic2(self):

        video_path = "static\Traffic2.mp4"
        output_folder = "ExtractedImageDataset2"
        if not os.path.exists(str(output_folder)):
            os.makedirs(str(output_folder))

        vidcap = cv2.VideoCapture(str(video_path))

        if not vidcap.isOpened():
            print("Error opening video file.")
            return

        count = 0

        while True:

            success, frame = vidcap.read()

            if not success:
                break

            filename = os.path.join(str(output_folder), f"traffic_2_{count}.jpg")
            cv2.imwrite(filename, frame)

            count += 1

        vidcap.release()
        return True

    def extract_file_list(self, path):
        fullpath_list = []
        dir_list = os.listdir(path)
        for file in dir_list:
            file = path + "/" + file
            fullpath_list.append(file)
        return fullpath_list

    def file_name_extractor(self, filepath):
        file_name = os.path.basename(filepath)
        return file_name

    def get_vehicle_count_details(self, image_path: str, functionality: str) -> dict:
        """_summary_

        Args:
            image_path (str): _description_
            functionality (str): _description_

        Returns:
            dict: _description_
        """

        vehicle_type_count = logic.process_image(image_path, functionality)
        return vehicle_type_count

    def get_truck_count(self, map):
        try:
            count = map["truck"]
        except:
            count = 0
        print(count)
        return count

    def track_truck_in_school_hrs(self, image_path: str, functionality: str) -> int:
        """_summary_

        Args:
            image_path (str): _description_
            functionality (str): _description_

        Returns:
            int: _description_
        """
        vehicle_type_count = logic.process_image(image_path, None)
        truck_count = self.get_truck_count(vehicle_type_count)
        if (
            self.time > self.today_8am
            and self.time < self.today_5pm
            and truck_count > 0
        ):
            logic.process_image(image_path, functionality)
            return vehicle_type_count["truck"]
        else:
            return False

    def track_violation(self, image_path: str, functionality: str) -> bool:
        """_summary_

        Args:
            image_path (str): _description_
            functionality (str): _description_

        Returns:
            bool: _description_
        """
        logic.process_image(image_path, functionality)
        return True

    def get_vehicle_count(
        self,
        junction1_data,
        junction2_data,
        junction3_data,
        junction4_data,
    ):

        try:
            cars = junction1_data["car"]
        except:
            cars = 0
        try:
            motorbike = junction1_data["motorbike"]
        except:
            motorbike = 0
        try:
            bus = junction1_data["bus"]
        except:
            bus = 0
        try:
            truck = junction1_data["truck"]
        except:
            truck = 0
        junction1_vehicle_count = cars + motorbike + bus + truck

        try:
            cars = junction2_data["car"]
        except:
            cars = 0
        try:
            motorbike = junction2_data["motorbike"]
        except:
            motorbike = 0
        try:
            bus = junction2_data["bus"]
        except:
            bus = 0
        try:
            truck = junction2_data["truck"]
        except:
            truck = 0
        junction2_vehicle_count = cars + motorbike + bus + truck

        try:
            cars = junction3_data["car"]
        except:
            cars = 0
        try:
            motorbike = junction3_data["motorbike"]
        except:
            motorbike = 0
        try:
            bus = junction3_data["bus"]
        except:
            bus = 0
        try:
            truck = junction3_data["truck"]
        except:
            truck = 0
        junction3_vehicle_count = cars + motorbike + bus + truck

        try:
            cars = junction4_data["car"]
        except:
            cars = 0
        try:
            motorbike = junction4_data["motorbike"]
        except:
            motorbike = 0
        try:
            bus = junction4_data["bus"]
        except:
            bus = 0
        try:
            truck = junction4_data["truck"]
        except:
            truck = 0
        junction4_vehicle_count = cars + motorbike + bus + truck

        return (
            junction1_vehicle_count,
            junction2_vehicle_count,
            junction3_vehicle_count,
            junction4_vehicle_count,
        )

    def control_traffic_light(
        junction1_vehicle_count,
        junction2_vehicle_count,
        junction3_vehicle_count,
        junction4_vehicle_count,
    ):
        pass
