import streamlit as st
import numpy as np
import cv2

# configure streamlite
st.set_page_config(layout="wide")



with st.container():
    col1, col2 = st.columns([3, 1])
    
    deviceTab, personTab = col2.tabs(["Device", "Person"])
    
    # rendering person
    personTab.title("Person")
    for c in range(0, 3):

        left, middle, right = personTab.columns(3, vertical_alignment="center")
        left.image("assets/image.jpg", use_column_width=True)
        middle.caption("unnamed")
        right.button("Rename", key="rename" + str(c))
        
    # rendering
    for c in range(0, 3):

        left, middle, right = deviceTab.columns(3, vertical_alignment="center")
        left.image("assets/image.jpg", use_column_width=True)
        middle.caption("Point 2")
        right.button("Open", key=c)
        
    
    
    
    # configure opencv
    cap = cv2.VideoCapture("video.mp4")
        
    col1.title("Streaming")
    isPlay = False
    stop_button_pressed = col1.button("Stop", key="stop")
    
    frame_placeholder = col1.empty()
    while not stop_button_pressed:
        ret, frame = cap.read()
        if not ret:
            col1.write("Video Capture Ended")
            continue
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB", use_column_width=True)
    
    cap.release()
    cv2.destroyAllWindows()