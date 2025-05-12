#####################
# IMPORTS
import streamlit as st
import pandas as pd
import numpy as np
import time
from calculations import Calculations
#####################

# streamlit run main.py

st.title("Data Analyzer")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")


if uploaded_file and st.button("Analyze"):

    progress_text = "Operation in progress..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    
    df = pd.read_csv(uploaded_file)
    df_clean = df.dropna()

    st.session_state.df_clean = df_clean

if "df_clean" in st.session_state:
    df_clean = st.session_state.df_clean

    st.write("Cleaned Data", df_clean.head())

    # Select numeric column to analyze
    numeric_cols = df_clean.select_dtypes(include='number').columns.tolist()
    selected_col = st.selectbox("Select column to analyze", numeric_cols)

if selected_col:
    calc = Calculations(df_clean)

    st.subheader("Statistics")

    option = st.selectbox("Select a calculation to perform", ["Mean", "Median", "Standard Deviation"])

    match option:
        case "Mean":
            mean = calc.mean(selected_col)
            st.write(f"Mean: {mean:.2f} (rounded)")
        case "Median":
            median = calc.median(selected_col)
            st.write(f"Median: {median}")
        case "Standard Deviation":
            deviation = calc.std_dev(selected_col)
            st.write(f"Standard Deviation: {deviation:.2f} (rounded)")














