import os
from flask import request


class Handlers:

    def handle_image_uploads(self):
        image_file = request.files["image"]
        image_path = os.path.join("case_studies", image_file.filename)
        image_file.save(image_path)
        return image_path, image_file.filename

    def handle_multiple_image_uploads(self):
        image_file_1 = request.files["junction1"]
        image_path_1 = os.path.join("case_studies", image_file_1.filename)
        image_file_1.save(image_path_1)
        image_file_2 = request.files["junction2"]
        image_path_2 = os.path.join("case_studies", image_file_2.filename)
        image_file_2.save(image_path_2)
        image_file_3 = request.files["junction3"]
        image_path_3 = os.path.join("case_studies", image_file_3.filename)
        image_file_3.save(image_path_3)
        image_file_4 = request.files["junction4"]
        image_path_4 = os.path.join("case_studies", image_file_4.filename)
        image_file_4.save(image_path_4)
        return (
            image_path_1,
            image_path_2,
            image_path_3,
            image_path_4,
        )

    def handle_violation_id(self):
        if request.method == "POST":
            id = request.form["id"]
            return id
