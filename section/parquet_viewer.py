import streamlit as st
import pandas as pd
from datetime import datetime

def page():
    st.title("File Uploader 📁")
    st.write("Welcome to the File Uploader app! This app allows you to upload a Parquet or a CSV file and view its contents.")
    st.write("To get started, click the button below to choose a file to upload.")

    uploaded_file = st.file_uploader("Choose a file to upload 📂",type = ['parquet','csv'])

    if uploaded_file is not None:
        if 'parquet' in uploaded_file.name: data = pd.read_parquet(uploaded_file)
        else : data = pd.read_csv(uploaded_file)

        #Display data
        st.write("Here's the contents of your file:")
        # format_data = "%H:%M:%S.%f"
        # data['Timestamp'] = datetime.strptime(data['Timestamp'], format_data)
        st.dataframe(data)

        #Analysis
        st.header("Some analysis")
        st.subheader("Mercure Data")
        Mercure_Hg_data = data[data["Element"]=="Mercure-Hg"]
        st.dataframe(Mercure_Hg_data)
        st.line_chart(Mercure_Hg_data, x="Timestamp", y="Value")


        st.subheader("Nickel Data")
        Nickel_Ni_data = data[data["Element"]=="Nickel-Ni"]
        st.dataframe(Nickel_Ni_data)
        st.line_chart(Nickel_Ni_data, x="Timestamp", y="Value")

        
        st.subheader("Chrome Data")
        Chrome_Cr_data = data[data["Element"]=="Chrome-Cr"]
        st.dataframe(Chrome_Cr_data)
        st.line_chart(Chrome_Cr_data, x="Timestamp", y="Value")

        st.subheader("Zinc Data")
        Zinc_Zn_data = data[data["Element"]=="Zinc-Zn"]
        st.dataframe(Zinc_Zn_data)
        st.line_chart(Zinc_Zn_data, x="Timestamp", y="Value")

        




    else:
        st.write("No file uploaded yet? Don't be shy, give it a try! 😉👍")