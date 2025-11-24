import streamlit as st
         
pages = {
    "Dashboard":[
        st.Page("dashboard.py",title="Dashboard"),
    ],
    "Event manage":[
        st.Page("event_manage.py",title="Event manage"),
        st.Page("add_event.py",title="Event create"),
        st.Page("attendance_record.py",title="Start event"),
        ],
    "Attendee manage":[
        st.Page("event_list.py",title="Event List for Attendees"),
        st.Page("add_person.py",title="Add Attendees"),
    ],
    "Location manage":[
        st.Page("location_list.py",title="Location list"),
        st.Page("add_location.py",title="Add new location"),
    ],
}
pg = st.navigation(pages)
pg.run()
         

    
