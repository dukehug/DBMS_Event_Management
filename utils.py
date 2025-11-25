import streamlit as st
import pandas as pd
import datetime
import pyodbc


#function connect to the databse
@st.cache_resource
def init_connection():
    return pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
    + st.secrets["server"]
    + ";DATABASE="
    + st.secrets["database"]
    + ";UID="
    + st.secrets["username"]
    + ";PWD="
    + st.secrets["password"]
    )

#read data 
@st.cache_data(ttl=600)
def run_query(query):
    
    conn = init_connection() 
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
         
#update data /  use different query syntax , you can insert,update,delete   
def execute_update(query,params):
    conn = init_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query,params) #query syntax and params
            conn.commit() #submit
            return True
    except Exception as e:
        st.error(f"Database Error: {e}")
        return False