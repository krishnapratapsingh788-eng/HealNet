import streamlit as st
import pandas as pd
from database.connection import get_connection


st.title("🧑‍⚕️ Patient Dashboard")


def load_patients():

    conn = get_connection()

    query = "SELECT * FROM patients"

    data = pd.read_sql(query, conn)

    conn.close()

    return data


try:
    patients = load_patients()

    st.success("Database Connected ✅")

    st.dataframe(
        patients,
        use_container_width=True
    )

except Exception as e:
    st.error(f"Error: {e}")