#####################
# IMPORTS
import streamlit as st
import pandas as pd
from calculations import Calculations
#####################

# streamlit run main.py

st.title("Data Analyzer")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")


if uploaded_file is not None:

    if st.button("Analyze"):

        df = pd.read_csv(uploaded_file)
        st.write("Raw Data", df.head())

        st.subheader("Removing Null values")

        df_clean = df.dropna()
        st.write("Cleaned Data", df_clean.head())

        # Select numeric column to analyze
        numeric_cols = df_clean.select_dtypes(include='number').columns.tolist()
        selected_col = st.selectbox("Select column to analyze", numeric_cols)




        calc = Calculations()
        mean = calc.mean(selected_col)
        median = calc.median(selected_col)

