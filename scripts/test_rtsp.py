import cv2

# RTSP URL - replace with your RTSP stream URL
rtsp_url = "rtsp://localhost:8554/live.sdp"
# rtsp_url = "video.mp4"

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Check if the video stream is opened successfully
if not cap.isOpened():
    print("Error: Unable to connect to RTSP stream.")
    exit()

# Read and display frames from the RTSP stream
while True:
    ret, frame = cap.read()
    
    # If frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to grab frame.")
        break
    
    # Display the frame
    cv2.imshow("RTSP Stream", frame)
    
    # Wait for key press to exit (press 'q' to quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()