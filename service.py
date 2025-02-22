import os
import base64
from datetime import datetime
from Engine.VisionLogic import logic


class Services:

    def __init__(self):

        self.time = datetime.now()
        self.today_8am = datetime(2025, 2, 22, 8, 0)
        self.today_10am = datetime(2025, 2, 22, 10, 50)

    def extract_file_list(self, path):
        fullpath_list = []
        dir_list = os.listdir(path)
        for file in dir_list:
            file = path + "/" + file
            fullpath_list.append(file)
        return fullpath_list

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

    def track_truck_in_school_hrs(self, image_path: str, functionality: str) -> int:
        """_summary_

        Args:
            image_path (str): _description_
            functionality (str): _description_

        Returns:
            int: _description_
        """
        vehicle_type_count = logic.process_image(image_path, functionality)
        if (
            self.time > self.today_8am
            and self.time < self.today_10am
            and vehicle_type_count["truck"] > 0
        ):
            return vehicle_type_count["truck"]
        else:
            return 0

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


# Services().track_violation("static/case_studies/2.png", "RED_SIGNAL_CROSSING")
# Services().track_violation("static/case_studies/4.jpeg", "NO_PARKING")
# Services().track_truck_in_school_hrs(
#     "static/case_studies/4.jpeg", "HEAVY_VEHICLES_SCHOOL_TIME"
# )
# data = Services().get_vehicle_count_details("static/case_studies/4.jpeg", None)
# print(data)
# Services().track_violation("static/case_studies/Tvm/ped_1.jpeg", "RED_SIGNAL_CROSSING")
