import streamlit as st

def show_header():

    col1, col2 = st.columns([1,5])

    with col1:
        st.image("assets/logo.png", width=90)

    with col2:
        st.markdown("""
        <h1 style='color:#1565C0;margin-bottom:0;'>
        🏥 HealNet 2.0
        </h1>

        <p style='color:gray;font-size:18px;'>
        AI Powered Smart Hospital Management System
        </p>
        """, unsafe_allow_html=True)

    st.divider()