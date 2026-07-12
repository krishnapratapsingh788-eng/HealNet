import streamlit as st

USERNAME = "admin"
PASSWORD = "healnet123"


def login():

    st.title("🔐 HealNet Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):

        if user == USERNAME and pwd == PASSWORD:

            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()

        else:

            st.error("Invalid Username or Password")