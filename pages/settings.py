import streamlit as st

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ HealNet Settings")

theme = st.selectbox(
    "Application Theme",
    [
        "Light",
        "Dark"
    ]
)

language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi"
    ]
)

notify = st.toggle("Enable Notifications",value=True)

email = st.text_input("Admin Email")

hospital = st.text_input("Hospital Name","HealNet Hospital")

location = st.text_input("Hospital Location","Lucknow")

st.divider()

if st.button("💾 Save Settings",use_container_width=True):
    st.success("Settings Saved Successfully")

st.info("HealNet 2.0 Professional Settings Module")