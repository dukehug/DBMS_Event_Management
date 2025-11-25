import streamlit as st

<<<<<<< HEAD

#page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Event management system",
                    layout="wide",
                )


=======
>>>>>>> 5f37323087f6b40cdffe5741a9ebaeb13cf52cc5
#streamlit navigation bar
#https://docs.streamlit.io/develop/api-reference/navigation/st.navigation
pages = {
    "Dashboard":[
        st.Page("dashboard.py",title="Dashboard"),
    ],
    "Event manage":[
        st.Page("event_manage.py",title="Event manage"),
        st.Page("add_event.py",title="Event create"),
        st.Page("attendance_record.py",title="Start event"),
        ],
    "Attendee Register manage":[
        st.Page("event_register_list.py",title="Event List for Attendees"),
        st.Page("add_person.py",title="Add Attendees"),
    ],
    "Location manage":[
        st.Page("location_list.py",title="Location list"),
        st.Page("add_location.py",title="Add new location"),
    ],
}
pg = st.navigation(pages)
pg.run()
         

    

