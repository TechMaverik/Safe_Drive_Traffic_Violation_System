import math
import cv2
import os


class EuclideanDistTracker:
    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0

    def update(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h, index = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    # print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id, index])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count, index])
                self.id_count += 1

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id, index = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()
        return objects_bbs_ids


class ViolationTracker:

    def file_name_extractor(self, filepath):
        file_name = os.path.basename(filepath)
        return file_name

    def red_signal_crossing(self, center, img, image_path):
        x, y = center
        if y > 560:
            cv2.line(img, (83, 560), (383, 560), (0, 0, 255), 1)
            cv2.circle(img, center, 2, (255, 0, 0), 10)
            cv2.putText(
                img,
                "Red Signal Violator",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
            )
            filename = self.file_name_extractor(image_path)
            cv2.imwrite("static/" + filename, img)

    def truck_in_schooltime(self, img, image_path):
        filename = self.file_name_extractor(image_path)
        cv2.imwrite("static/" + filename, img)

    def no_parking(self, center, img, image_path):
        x, y = center
        if (-412 * x + 156 * y < -57932) and (-139 * x + 100 * y > -15632):
            cv2.line(img, (241, 259), (385, 646), (0, 0, 255), 1)
            cv2.line(img, (288, 244), (388, 383), (0, 0, 255), 1)
            cv2.circle(img, center, 2, (0, 0, 255), 1)
            cv2.putText(
                img,
                "NO PARKING Violator",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
            )
            filename = self.file_name_extractor(image_path)
            cv2.imwrite("static/" + filename, img)

    def vehicle_zebra_crossing(self, center, img, image_path):
        x, y = center
        if (y > 628) and (y < 668):
            cv2.line(img, (0, 628), (472, 628), (255, 0, 0), 4)
            cv2.line(img, (0, 668), (472, 668), (255, 0, 0), 4)
            cv2.circle(img, center, 2, (0, 0, 255), 10)
            cv2.putText(
                img,
                "ZEBRA CROSSING Violator",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
            )
            filename = self.file_name_extractor(image_path)
            cv2.imwrite("static/" + filename, img)

    def pedestrian_crossing(self, center, img, image_path):
        x, y = center
        if (-432 * x + 202 * y < -364332) and (-222 * x + 183 * y > -180327):
            cv2.line(img, (1065, 474), (1267, 906), (0, 0, 255), 9)
            cv2.circle(img, center, 2, (0, 0, 255), 10)
            cv2.putText(
                img,
                "PEDESTRIAN Violator",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
            )
            filename = self.file_name_extractor(image_path)
            cv2.imwrite("static/" + filename, img)
