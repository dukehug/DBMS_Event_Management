import streamlit as st
from utils import run_query



#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Event Management Systemt",
                    layout="wide",
                )

st.title("Event management system")
st.write("Welcome to back  - dashboard.py")
st.divider()

# dashboard
st.subheader("Event Summary")
