import streamlit as st

def show_sidebar():
    with st.sidebar:

        st.image("assets/logo.png", width=90)

        st.title("HealNet 2.0")

        st.markdown("---")

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "👤 Patients",
                "👨‍⚕️ Doctors",
                "📅 Appointments",
                "🤖 AI Agent",
                "📊 Analytics",
                "🚑 Emergency",
                "⚙ Settings"
            ]
        )

        st.markdown("---")

        st.success("🟢 System Online")

        return page