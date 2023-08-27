import cv2
import mediapipe as mp

# Initialize MediaPipe drawing utilities and Pose model
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open the video file
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    # Read frame from the video capture
    _, frame = cap.read()
    try:
        # Resize the frame for portrait video (commented out for webcam)
        # frame = cv2.resize(frame, (350, 600))
        
        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for pose detection
        pose_results = pose.process(frame_rgb)

        # Draw skeleton on the frame
        mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Display the frame with pose landmarks
        cv2.imshow('Output', frame)
    except:
        break

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Accessing specific landmark (landmark index 32)
pose_landmark_32 = pose_results.pose_landmarks.landmark[32]

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame from the webcam
    _, frame = cap.read()
    try:
        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for pose detection
        pose_results = pose.process(frame_rgb)

        # Draw skeleton on the frame
        mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Display the frame with pose landmarks
        cv2.imshow('Output', frame)
    except:
        break

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
