import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts():

    st.subheader("📊 Hospital Analytics")

    col1, col2 = st.columns(2)

    with col1:
        df = pd.DataFrame({
            "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
            "Patients": [120,150,180,220,260,310]
        })

        fig = px.line(
            df,
            x="Month",
            y="Patients",
            markers=True,
            title="Patient Growth"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        disease = pd.DataFrame({
            "Disease":["Fever","Diabetes","BP","Heart","Others"],
            "Patients":[35,25,15,10,15]
        })

        fig2 = px.pie(
            disease,
            names="Disease",
            values="Patients",
            title="Disease Distribution"
        )

        st.plotly_chart(fig2, use_container_width=True)