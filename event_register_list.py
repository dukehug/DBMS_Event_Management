import streamlit as st
import pandas as pd
import pyodbc
from utils import run_query, execute_update

#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Event list for Adttendee",
                    layout="wide",
                )
st.title("Event list for Adttendee")
st.write("Welcome to Event event_register_list.py")
st.divider()

