import streamlit as st
import pandas as pd
import pyodbc
from utils import run_query, execute_update

#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Start Event",
                    layout="wide",
                )
st.title("Start Event")
st.write("Welcome to Event attendance_record.py")
st.divider()