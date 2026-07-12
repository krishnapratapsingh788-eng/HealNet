import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Doctors | HealNet 2.0",
    page_icon="👨‍⚕️",
    layout="wide"
)

st.title("👨‍⚕️ Doctor Management")
st.caption("Manage Hospital Doctors")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Doctors", "48", "+2")

with c2:
    st.metric("Available", "40")

with c3:
    st.metric("On Leave", "5")

with c4:
    st.metric("Emergency Duty", "3")

st.divider()

search = st.text_input("🔍 Search Doctor")

doctors = pd.DataFrame({
    "Doctor ID":["DR101","DR102","DR103","DR104","DR105"],
    "Name":["Dr. Sharma","Dr. Khan","Dr. Gupta","Dr. Mehta","Dr. Singh"],
    "Specialization":["Cardiology","Neurology","Orthopedic","General","Dermatology"],
    "Experience":["10 Years","8 Years","12 Years","6 Years","9 Years"],
    "Status":["Available","Busy","Available","On Leave","Available"]
})

if search:
    doctors = doctors[doctors["Name"].str.contains(search, case=False)]

st.dataframe(doctors, use_container_width=True, hide_index=True)

st.divider()

doctor = st.selectbox("Select Doctor", doctors["Name"])

row = doctors[doctors["Name"] == doctor].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Doctor Information")
    st.write(f"**ID:** {row['Doctor ID']}")
    st.write(f"**Name:** {row['Name']}")
    st.write(f"**Specialization:** {row['Specialization']}")

with col2:
    st.subheader("Professional Details")
    st.write(f"**Experience:** {row['Experience']}")
    st.write(f"**Status:** {row['Status']}")

st.divider()

a, b, c = st.columns(3)

with a:
    st.button("➕ Add Doctor", use_container_width=True)

with b:
    st.button("✏ Edit Doctor", use_container_width=True)

with c:
    st.button("🗑 Remove Doctor", use_container_width=True)

st.success("✔ HealNet Doctor Module Ready")