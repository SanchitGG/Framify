import cv2
import os
def video2frame(video_path,number_of_intervals):
    def __init__(self):
        self.video_path=video_path
        self.number_of_intervals=number_of_intervals
    def __call__ (self):
        cap = cv2.VideoCapture(self.video_path)

        # Get frames per second (FPS) and total frame count
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames // fps  # Duration in seconds

        # Create a folder to save frames
        output_folder = "frames"
        os.makedirs(output_folder, exist_ok=True)
        # Extract frames every 30 seconds
        interval = self.number_of_intervals
        frame_number = 0
        frame_count = 0

        while frame_number < total_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  # Set position to specific frame
            ret, frame = cap.read()

            if not ret:
                break  # Break loop if unable to read frame

            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")

            frame_count += 1
            frame_number += fps * interval  # Move to the next 30-second mark

        # Release video capture
        cap.release()
        cv2.destroyAllWindows()
        print("Frame extraction completed!")

