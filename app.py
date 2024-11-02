import streamlit as st

pages = {
    "Home": [
        st.Page("pages/preview.py", title="Preview"),
        # st.Page("manage_account.py", title="Manage your account"),
    ],
}

pg = st.navigation(pages)
pg.run()