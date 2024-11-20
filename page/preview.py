import streamlit as st
import numpy as np
import cv2

import core

rtsp_url = "rtsp://localhost:8554/live.sdp"

def start_stream():
    if not st.session_state.is_streaming:
        st.session_state.cap = cv2.VideoCapture(rtsp_url)
        st.session_state.is_streaming = True

if "is_streaming" not in st.session_state:
    st.session_state.is_streaming = False

# Function to stop the video stream
def stop_stream():
    if st.session_state.is_streaming:
        st.session_state.is_streaming = False
        if st.session_state.cap is not None:
            st.session_state.cap.release()
            st.session_state.cap = None


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
        
    
    
    
    
        
    col1.title("Streaming")
    
    
    # startc, stopc = col1.columns([1, 1])
    start_button = col1.button("Start", key="start")
    stop_button = col1.button("Stop", key="stop")

    if start_button:
        start_stream()

    if stop_button:
        stop_stream()

    frame_placeholder = col1.empty()
    # tampil di layar
    def show_image(frame):
        if frame_placeholder:
            frame_placeholder.image(frame, channels="RGB", use_column_width=True)


    core.stream_detect.sink(show_image)


    while st.session_state.is_streaming and st.session_state.cap.isOpened():
        ret, frame = st.session_state.cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        core.emit_frame(frame=frame)

    