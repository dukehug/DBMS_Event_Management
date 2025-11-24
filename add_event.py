import streamlit as st
import datetime
from utils import run_query,execute_adddata


st.set_page_config(layout="wide")
st.title("Add new Event")
st.write("Check all infomation are correct")
st.divider()

#use try except get data from table Location 
try:
    localtions_data = run_query("SELECT location_id,loc_name FROM Location")
    
    #create a mapping
    location_options = {row[1]:row[0] for row in localtions_data}
    
except Exception as e:
    st.error(f"Can't get location data , plz check Location table. Erro:{e}")
    location_options = {}


#create a form for fill 
with st.form("add_event_form"):
    
    col1,col2 = st.columns(2) #form side by side
    with col1:
        new_evn_name = st.text_input("Event Name")
        new_evn_type = st.selectbox("Event Type",["Public","Private"])
        new_evn_organizer = st.text_input("Organizer")
        
        #select location name
        selected_location_name = st.selectbox("Location",list(location_options.keys()))
    with col2:
        new_start_date = st.date_input("Start Date",datetime.date.today())
        new_end_date = st.date_input("End Date",datetime.date.today())
        new_evn_desc = st.text_area("Description", height=100)
    
    submited_btn = st.form_submit_button("Submit Event")
    
    if submited_btn:
        if not new_evn_name or not selected_location_name:
            st.warning("Please fill in the Event Name and Location.")
        else:
            final_location_id = location_options[selected_location_name]
            sql_query= """
                INSERT INTO Event
                (location_id,evn_name,evn_start_date,evn_end_date,evn_organizer,evn_description,evn_type)
                VALUES (?,?,?,?,?,?,?)
            """
            params = (
                final_location_id,
                new_evn_name,
                new_start_date,
                new_end_date,
                new_evn_organizer,
                new_evn_desc,
                new_evn_type
            )
            
            if execute_adddata(sql_query,params):
                st.success(f"Success! Event '{new_evn_name}' has been added.")
                #st.rerun()
    