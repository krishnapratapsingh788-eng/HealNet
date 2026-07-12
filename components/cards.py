import streamlit as st

def dashboard_cards():

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="👥 Total Patients",
            value="1,254",
            delta="+15 Today"
        )

    with c2:
        st.metric(
            label="👨‍⚕️ Doctors",
            value="48",
            delta="+2"
        )

    with c3:
        st.metric(
            label="📅 Appointments",
            value="89",
            delta="+12 Today"
        )

    with c4:
        st.metric(
            label="🤖 AI Reports",
            value="352",
            delta="+28"
        )