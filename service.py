from datetime import datetime
from Engine.VisionLogic import logic


class Services:

    def __init__(self):
        self.time = datetime.now()
        self.today_8am = datetime(2025, 2, 16, 17, 0)
        self.today_10am = datetime(2025, 2, 16, 19, 0)

    def get_vehicle_count_details(self, image_path):
        vehicle_type_count = logic.from_static_image(image_path)
        return vehicle_type_count

    def track_heavy_hehicle_in_school_hrs(self, image_path):
        vehicle_type_count = logic.from_static_image(image_path)
        if (
            self.time > self.today_8am
            and self.time < self.today_10am
            and vehicle_type_count["truck"] > 0
        ):
            return "Truck Found"
        else:
            return "Truck Not Found"
