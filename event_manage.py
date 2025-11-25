import streamlit as st
import pandas as pd
import pyodbc
from utils import run_query, execute_update

#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Event list for Manage",
                    layout="wide",
                )
st.title("Event manage")
st.write("Welcome to Event manage event_manage.py  /  event search, display , edit, delete, quick add")
st.divider()