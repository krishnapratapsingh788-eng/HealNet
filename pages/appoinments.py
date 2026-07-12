import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Appointments | HealNet",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Appointment Management")

appointments = pd.DataFrame({
    "Appointment ID":["A101","A102","A103","A104"],
    "Patient":["Rahul","Priya","Aman","Sneha"],
    "Doctor":["Dr. Sharma","Dr. Khan","Dr. Gupta","Dr. Mehta"],
    "Date":["12 Jul","12 Jul","13 Jul","13 Jul"],
    "Time":["10:00 AM","11:30 AM","2:00 PM","4:00 PM"],
    "Status":["Confirmed","Pending","Completed","Confirmed"]
})

st.dataframe(appointments, use_container_width=True, hide_index=True)

st.divider()

st.subheader("Book Appointment")

with st.form("appointment"):

    patient = st.text_input("Patient Name")
    doctor = st.selectbox(
        "Doctor",
        ["Dr. Sharma","Dr. Khan","Dr. Gupta","Dr. Mehta"]
    )

    date = st.date_input("Appointment Date")
    time = st.time_input("Appointment Time")

    submit = st.form_submit_button("Book Appointment")

if submit:
    st.success(f"Appointment booked successfully for {patient}.")