import streamlit as st
import requests
from components.sidebar import show_sidebar
from components.header import show_header
from components.cards import dashboard_cards
from components.charts import show_charts
from database.database import create_tables, add_patient

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="HealNet AI",
    page_icon="🏥",
    layout="wide"
)

# ---------------- LOAD CSS ----------------

def load_css():
    with open("styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
create_tables()
show_sidebar()
show_header()
dashboard_cards()
show_charts()

# ---------------- HEADER ----------------

# ---------------- WEBHOOK ----------------

WEBHOOK_URL = "http://localhost:5678/webhook-test/healnet-patient"

# ---------------- FORM ----------------

with st.form("patient_form"):

    col1,col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Full Name")
        age = st.number_input("🎂 Age",1,120)
        gender = st.selectbox("⚧ Gender",["Male","Female","Other"])
        phone = st.text_input("📞 Phone")

    with col2:

        email = st.text_input("📧 Email")
        symptoms = st.text_area("🤒 Symptoms")
        diseases = st.text_area("🩺 Existing Diseases")
        medicines = st.text_area("💊 Current Medicines")

    submit = st.form_submit_button("📝 Register Patient")

# ---------------- SUBMIT ----------------

if submit:

    patient_message = f"""
Patient Registration

Name: {name}
Age: {age}
Gender: {gender}
Phone: {phone}
Email: {email}

Symptoms:
{symptoms}

Existing Diseases:
{diseases}

Current Medicines:
{medicines}

Analyze this patient and provide:

1. Registration Confirmation
2. Patient Summary
3. Possible Health Concerns
4. Recommended Specialist Doctor
5. General Health Advice

Keep the answer short and professional.
"""

    try:

        response = requests.post(
            WEBHOOK_URL,
            json={
                "message": patient_message
            }
        )

        if response.status_code == 200:
            add_patient(name,age,gender,phone,email,symptoms,diseases,medicines)

            st.success("✅ Patient Registered Successfully!")

            st.markdown("<div class='ai-card'>",unsafe_allow_html=True)

            st.subheader("🤖 AI Health Report")

            try:

                data=response.json()

                if "output" in data:
                    st.write(data["output"])
                else:
                    st.json(data)

            except:
                st.write(response.text)

            st.markdown("</div>",unsafe_allow_html=True)

        else:

            st.error(f"Webhook Error : {response.status_code}")
            st.write(response.text)

    except Exception as e:

        st.error(f"Connection Error : {e}")

# ---------------- PATIENT DETAILS ----------------

st.divider()

st.subheader("📋 Patient Details")

c1,c2 = st.columns(2)

with c1:
    st.write(f"**👤 Name:** {name}")
    st.write(f"**🎂 Age:** {age}")
    st.write(f"**⚧ Gender:** {gender}")
    st.write(f"**📞 Phone:** {phone}")

with c2:
    st.write(f"**📧 Email:** {email}")
    st.write(f"**🤒 Symptoms:** {symptoms}")
    st.write(f"**🩺 Diseases:** {diseases}")
    st.write(f"**💊 Medicines:** {medicines}")

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
❤️ Developed by Krishna Pratap Singh
</div>
""",unsafe_allow_html=True)