import streamlit as st

def page():
    st.title("About This App 🤖")
    st.write("Welcome to the Data Generator and File Uploader app! This app is designed for data scientists and engineers who need a quick and easy way to generate random datasets and upload existing data files.")
    st.write("The data generator feature allows you to generate a dataset with timestamps, elements (Hg, Ni, Cr, or Zn), and random values between 0 and 100. You can specify the number of rows to generate and choose to save the data as a CSV or Parquet file.")
    st.write("The file uploader feature allows you to upload an existing Parquet or CSV file and view its contents. This can be useful if you need to quickly inspect a file or extract data from it.")
    st.write("You can save your creations to Azure Blob for safekeeping 🚀👨‍💻. So go ahead  🙌😎")
    st.write("This app was built using Streamlit, a Python library for building web applications. The data generator and file uploader functionalities were implemented using Pandas, a powerful data analysis library for Python.")
    
    st.write("We hope this app will be a useful tool for your data projects. If you have any feedback or suggestions, please don't hesitate to reach out to us.")
    
    st.write("Thank you for using our app! 🚀📈")