import streamlit as st
import numpy as np

# configure streamlite
st.set_page_config(layout="wide")


with st.container():
    

    data = np.random.randn(10, 1)



    col1, col2 = st.columns([3, 1])
    col1.title("Streaming")
    col1.camera_input("CCTV Detection", disabled=True)

    col2.title("Person")
    for c in range(0, 3):

        left, middle, right = col2.columns(3, vertical_alignment="center")
        left.image("assets/image.jpg", use_column_width=True)
        middle.caption("unnamed")
        right.button("Rename", key=c)
        