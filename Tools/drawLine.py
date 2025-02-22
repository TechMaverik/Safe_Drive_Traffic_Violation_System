# Python program to explain cv2.line() method

# importing cv2
import cv2

# path
path = "/home/techmaverik/Pro/Safe_Drive_Traffic_Violation_System/static/case_studies/1.jpeg"

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = "Image"

# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (925, 586)

# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (1123, 948)

# Green color in BGR
color = (0, 255, 0)

# Line thickness of 9 px
thickness = 9

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
