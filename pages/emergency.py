import streamlit as st

st.set_page_config(
    page_title="Emergency SOS",
    page_icon="🚑",
    layout="wide"
)

st.title("🚑 Emergency Dashboard")

st.error("Emergency Monitoring System")

col1,col2,col3=st.columns(3)

col1.metric("Critical Patients","7")
col2.metric("Available Ambulance","5")
col3.metric("Emergency Doctors","12")

st.divider()

st.subheader("Emergency Contacts")

st.table({
    "Department":[
        "Ambulance",
        "ICU",
        "Police",
        "Fire",
        "Blood Bank"
    ],
    "Phone":[
        "108",
        "1800123456",
        "112",
        "101",
        "1800111111"
    ]
})

st.divider()

if st.button("🚨 SEND SOS",use_container_width=True):
    st.success("Emergency Alert Sent Successfully")

st.warning("Use only in real emergency situations.")