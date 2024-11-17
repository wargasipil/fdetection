import streamlit as st
import core

st.header("Register Face")
photo, camera = st.tabs(["Camera", "Photo"])

with camera:
    head = camera.container()
    labelc = camera.empty()
    label = labelc.text_input("Person Name:", "")
    camerac = camera.empty()
    picture = camera.camera_input("Take Photo", disabled=label=="")
    
    if picture:
        core.register_face(picture.getbuffer(), label=label)
        head.success("Registering Face Success")




# bagian upload file
with photo:
    uploaded_files = photo.file_uploader(
        "Choose a Photo File", accept_multiple_files=True
    )

    if uploaded_files is not None:
        for file in uploaded_files:
            image = file.getvalue()