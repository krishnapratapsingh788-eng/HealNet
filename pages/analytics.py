import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analytics | HealNet 2.0",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Hospital Analytics Dashboard")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Patients",1286,"+18")
c2.metric("Doctors",48,"+2")
c3.metric("Appointments",324,"+22")
c4.metric("Emergency",7,"-2")

st.divider()

st.subheader("Monthly Patient Statistics")

chart = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul"],
    "Patients":[220,280,350,410,500,610,720]
})

st.line_chart(chart.set_index("Month"))

st.subheader("Department Wise Patients")

pie = pd.DataFrame({
    "Department":["Cardiology","Neurology","Orthopedic","General","Dermatology"],
    "Patients":[120,80,60,240,100]
})

st.bar_chart(pie.set_index("Department"))

st.success("✔ Analytics Module Ready")