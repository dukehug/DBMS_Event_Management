import streamlit as st
import pandas as pd
import pyodbc
from utils import run_query, execute_adddata

#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Add new Attendee",
                    layout="wide",
                )
st.title("Add new Attendee")
st.write("Welcome to Event add_person.py")
st.divider()