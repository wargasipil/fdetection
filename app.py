import streamlit as st

st.set_page_config(layout="wide")

pages = {
    "Home": [st.Page("page/preview.py", title="Preview")],
    "Face": [
        st.Page("page/register_face.py", title="Register Face"),
        st.Page("page/setting.py", title="Setting"),
    ],
  
}

pg = st.navigation(pages)
pg.run()