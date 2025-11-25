import streamlit as st
import pandas as pd
import pyodbc
from utils import run_query, execute_update


#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Location list",
                    layout="wide",
                )
st.title("Location List")
st.write("Welcome to Event location_list.py")
st.divider()

# sreach columns
col_search, col_add = st.columns([3,1])

with col_search:
    search_term = st.text_input("Search by Location name", placeholder="Type to search")


#quick add
with col_add:
    st.write("") #space
    st.write("")
    if st.button("Quick Add", use_container_width=True):
        st.switch_page("add_location.py") #switch to add location
st.divider()

#process data 
try:
    #select data from table Location 
    fetch_sql ="""
        SELECT location_id,loc_name,loc_type,loc_capacity,
        loc_address,loc_contact_person,loc_contact_phone,loc_status
        FROM Location
    """
    
    rows = run_query(fetch_sql)
    
    
    #defin  columns header name
    columns = ["ID","Name","Type","Capacity","Address","Contact Person","Phone","Status"]
    df = pd.DataFrame.from_records(rows,columns=columns)
    
    
    #sreach  and filter 
    if search_term:
        
        # filter,  case insensitive
        df = df[df["Name"].str.contains(search_term,case=False,na=False)]
        
        #sql method
        ###
        #if search_term:
        #   sql = "SELECT * FROM Location WHERE loc_name LIKE ?"
        #   params = (f"%{search_term}%",)
        #   rows = run_query(sql, params)
        #else:
        #   rows = run_query("SELECT * FROM Location")
        ###
        
        
    st.caption(f"Find {len(df)} Location")
    
    
    
    
    #display data
    event = st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        selection_mode="single-row",
        on_select="rerun"   #笔记
    )
    
    # if selected 
    if len(event.selection.rows) > 0:
        #get selected row
        selected_index = event.selection.rows[0]
        selected_row = df.iloc[selected_index]  #笔记
        
        #get row id 
        current_id = int(selected_row["ID"])
        current_name = selected_row["Name"]
        
        #show info 
        st.info(f"You selected: **{current_name}**")
        
        #use tab, display feature and update,delete ,details
        
        tab_view, tab_edit, tab_delete = st.tabs(["Location Details","Update Location","Delete Location"])
        
        #tab 1 details 
        with tab_view:
            st.json(selected_row.to_dict())
            
        #tab 2 update 
        with tab_edit:
            with st.form("edit_location_form"):
                c1,c2 = st.columns(2)
                with c1:
                    #old data
                    new_name = st.text_input("Location Name", value=selected_row["Name"])
                    new_type = st.selectbox("Type", ["Out door", "In door"], index=0 if selected_row["Type"] == "Out door" else 1)
                    new_cap = st.text_input("Capacity", value=selected_row["Capacity"])
                    new_status = st.selectbox("Status", ["Available", "Unavailable"], index=0 if selected_row["Status"] == "Available" else 1)
                with c2:
                    new_person = st.text_input("Contact Person", value=selected_row["Contact Person"])
                    new_phone = st.text_input("Phone", value=selected_row["Phone"])
                    new_addr = st.text_area("Address", value=selected_row["Address"], height=108)
                
                #save
                update_btn = st.form_submit_button("SAVE")
                
                if update_btn:
                    update_sql = """
                        UPDATE Location
                        SET loc_name=?,loc_type=?,loc_capacity=?,loc_status=?,
                            loc_contact_person=?, loc_contact_phone=?, loc_address=?
                        WHERE location_id=?
                    """
                    params = (new_name, new_type, new_cap, new_status, new_person, new_phone, new_addr, current_id)
                    
                    if execute_update(update_sql,params):
                        st.success("Edited!")
                        st.rerun() # refresh 
                
        #delete tab        
        with tab_delete:
            st.warning(f"Are you sure want to delete '{current_name}' ??!!!")
            
            #double check 
            if st.button("Confirm", type="primary"):
                
                #check_sql = "SELECT COUNT(*) FROM Event WHERE location_id = ?" #if this location is use on event , can't delete
                
                delete_sql = "DELETE FROM Location WHERE location_id = ?"
                if execute_update(delete_sql,(current_id,)):
                    st.success(f"Location: '{current_name}' Deletion successful")
                    st.rerun()
                    
    elif len(df) > 0:
        st.info("Plz Choice 1 row")


except Exception as e:
    st.error(f"We got a error: {e}")
    
    

    
    