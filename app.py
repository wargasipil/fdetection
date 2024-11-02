import streamlit as st

pages = {
    "Home": [st.Page("page/preview.py", title="Preview")],
    "Face": [st.Page("page/register_face.py", title="Register Face")],
  
}

pg = st.navigation(pages)
pg.run()