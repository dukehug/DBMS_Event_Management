import streamlit as st
import pandas as pd
import pyodbc
from utils import run_query, execute_adddata

st.set_page_config(layout="wide")
st.title("Hello, there!")
st.write("Welcome to Event event_list.py")
st.divider()

