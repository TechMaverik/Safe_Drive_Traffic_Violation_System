import cv2


def click_event(event, x, y, flags, param):
    """
    This function is called when a mouse event occurs.
    It prints the coordinates of the clicked point and draws a circle on the image.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pixel coordinates: ({x}, {y})")
        # You can add more actions here, like storing the coordinates in a list
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # Draw a red circle
        cv2.imshow("image", img)  # Update the image to show the circle


# Load the image
img = cv2.imread("", 1)  # Replace 'image.jpg' with your image file

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image. Please check the file path.")
    exit()

cv2.imshow("image", img)

# Set the callback function for mouse events
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
