import cv2
import os

def extract_frames(video_path, output_folder, base_name):
    

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frame_number = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Use the base_name to create the frame file name
        frame_filename = os.path.join(output_folder, f"{base_name}_{frame_number:04d}.png")
        
        # Save the frame as an image
        cv2.imwrite(frame_filename, frame)
        
        frame_number += 1
    
    cap.release()

# Example usage

video_path = "/Downloads/i_001.mp4"  # Your video file path
# Extract the first word from the filename (before the first '_')
video_name = os.path.basename(video_path)  # get the file name (e.g., 'go_001.mp4')
base_name = video_name.split('_')[0]
output_folder = f"frames/{base_name}"  # Folder to save the frames
extract_frames(video_path, output_folder, base_name)
