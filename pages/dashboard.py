import streamlit as st

st.set_page_config(
    page_title="HealNet Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#06B6D4);
padding:25px;
border-radius:18px;
color:white;
margin-bottom:20px;">
<h1>🏥 HealNet 2.0 Dashboard</h1>
<p>AI Powered Smart Hospital Management System</p>
</div>
""", unsafe_allow_html=True)

# ================= Metrics =================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👤 Total Patients", "1,286", "+15 Today")

with col2:
    st.metric("👨‍⚕️ Doctors", "48", "+2 Available")

with col3:
    st.metric("📅 Appointments", "97", "12 Pending")

with col4:
    st.metric("🚑 Emergency", "4", "-1 Resolved")

st.divider()

# ================= Dashboard =================

left, right = st.columns([2,1])

with left:

    st.subheader("📊 Hospital Overview")

    st.info("""
✅ Total Registered Patients

✅ Daily OPD

✅ AI Health Reports

✅ Emergency Monitoring

✅ Smart Appointment System
""")

    st.subheader("📋 Recent Patients")

    st.dataframe({
        "Patient":["Rahul","Aman","Priya","Sneha","Rohit"],
        "Age":[22,34,28,45,31],
        "Status":["Healthy","Observation","Critical","Recovered","Healthy"]
    }, use_container_width=True)

with right:

    st.subheader("⚡ Quick Actions")

    if st.button("➕ Register Patient", use_container_width=True):
        st.success("Open Patient Registration Page")

    if st.button("🤖 AI Health Report", use_container_width=True):
        st.success("Opening AI Assistant")

    if st.button("📅 Book Appointment", use_container_width=True):
        st.success("Opening Appointment Module")

    if st.button("🚑 Emergency SOS", use_container_width=True):
        st.error("Emergency Module Opened")

st.divider()

st.subheader("📢 Hospital Announcement")

st.success("""
✔ AI Server Online

✔ Database Connected

✔ All Hospital Services Running Normally
""")

st.markdown("""
<hr>
<center>
❤️ Developed by Krishna Pratap Singh | HealNet 2.0
</center>
""", unsafe_allow_html=True)