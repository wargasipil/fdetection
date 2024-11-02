import streamlit as st

st.header("Register Face")
camera, photo = st.tabs(["Camera", "Photo"])

camera.camera_input("Take Photo", disabled=True)


uploaded_files = photo.file_uploader(
    "Choose a Photo File", accept_multiple_files=True
)