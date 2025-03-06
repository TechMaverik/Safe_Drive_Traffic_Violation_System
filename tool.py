import cv2
import os

def video_to_images(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize video capture
    vidcap = cv2.VideoCapture(video_path)
    
    # Check if video file was opened successfully
    if not vidcap.isOpened():
        print("Error opening video file.")
        return

    # Initialize frame counter
    count = 0

    while True:
        # Read frame
        success, frame = vidcap.read()
        
        if not success:
            break

        # Save frame as image
        filename = os.path.join(output_folder, f"frame_{count}.jpg")
        cv2.imwrite(filename, frame)
        
        # Increment frame counter
        count += 1

    # Release video capture
    vidcap.release()

    print(f"Extracted {count} frames.")

# Example usage
video_path = 'static\Traffic.mp4'
output_folder = 'ExtractedImageDataset'
video_to_images(video_path, output_folder)
