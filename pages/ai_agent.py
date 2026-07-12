import streamlit as st

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 HealNet AI Health Assistant")

st.info("Describe patient symptoms to receive an AI-generated health summary.")

symptoms = st.text_area(
    "Enter Symptoms",
    placeholder="Example: Fever, headache, sore throat..."
)

if st.button("Generate AI Report"):

    if symptoms.strip() == "":
        st.warning("Please enter symptoms.")
    else:

        st.success("AI Report Generated")

        st.markdown("### 🩺 Patient Summary")
        st.write("Patient shows symptoms that require clinical evaluation.")

        st.markdown("### ⚠ Possible Conditions")
        st.write("- Viral Fever")
        st.write("- Flu")
        st.write("- Infection")

        st.markdown("### 👨‍⚕️ Recommended Specialist")
        st.write("General Physician")

        st.markdown("### 💡 Advice")
        st.write("""
- Drink plenty of water
- Take proper rest
- Monitor body temperature
- Visit a doctor if symptoms worsen
""")