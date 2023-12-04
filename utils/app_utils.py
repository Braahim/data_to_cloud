import streamlit as st
import os
import os,uuid
from io import StringIO, BytesIO
import pyarrow as pa
import pyarrow.parquet as pq
# Define a function to save the dataframe to a file

# Define a function to save the dataframe to a file
def save_data(df, file_format):
    filename = st.text_input("Enter a filename:", value="data")
    if st.button("Save data"):
        filetypes = [("CSV files", "*.csv"), ("Parquet files", "*.parquet")]
        file = st.file_uploader("Choose a file", type=filetypes, key="fileUploader")
        if file is not None:
            with open(file.name, "wb") as f:
                f.write(file.read())
            st.success(f"File saved as {os.path.basename(file.name)}!")

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


def upload_to_blob(blob_client,df,file_format):
    # Create a local directory to hold blob data
    
    local_path = "./tmp"
    #os.mkdir(local_path)
    if file_format == 'csv':
        buffer = StringIO()
        df =  df.to_csv(buffer, header = 0, index = False)
        buffer.seek(0)
        blob_client.upload_blob(data=buffer.getvalue())
        st.warning("\nUploading to Azure Storage as blob CSV\n\t")
        
    else:
        parquet_file = BytesIO()
        df = df.to_parquet(parquet_file, engine="pyarrow")
        parquet_file.seek(0)
        blob_client.upload_blob(data=parquet_file)

        st.warning("\nUploading to Azure Storage as blob Parquet\n\t")


