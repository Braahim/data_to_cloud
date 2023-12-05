import streamlit as st
from utils import generate_utils, app_utils
import datetime


def page():
    st.title("Data Generator 🎲")
    st.write("Welcome to the Data Generator app! This app allows you to generate random data and save it as a CSV or Parquet file.")
    st.write("To get started, enter the number of files and lines per files you want to generate below and click the 'Let's go !' button.")
 

    num_files = st.slider("Enter the number of files to generate", value=10, min_value=1, max_value=10)
    num_lines = st.number_input("Enter the number of lines to generate", value=10, min_value=1, max_value=10000)

    
    st.session_state.button = st.button("Let's go ! ")
    if st.session_state.button:

        # Generate the data and display it in a table

        with st.spinner('wait for '+str(num_lines*0.5)+' seconds ...'):

            data = generate_utils.generate_data(num_lines)

            st.dataframe(data)


        csv = app_utils.convert_df(data)

        parquet = data.to_parquet()
        st.write("To save the data, use the buttons below to download it in CSV or Parquet format.")


        st.download_button(
        "Download Parquet 📈",
        parquet,
        "file.parquet",
        key='download-parquet'
        )

        st.download_button(
        "Download CSV 📊",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
        )

    st.header("Add Generated file to BLOB")
    if 'blob_service_client' not in st.session_state:
        st.warning('Please go to Connect to Azure section to add to Blob')
    else: 
        all_containers = st.session_state.blob_service_client.list_containers()
    
        containers = ['Choose container'] + list([x['name'] for x in all_containers])
        if 'data_container' not in st.session_state:
            st.session_state.data_container = containers[0]
        st.session_state.data_container = st.selectbox('Destination Container', containers, index = containers.index(st.session_state.data_container))
        if st.session_state.data_container == containers[0]:
            st.error('Please choose a container')
        else:
            #display container info
            container_client = st.session_state.blob_service_client.get_container_client(st.session_state.data_container)
            #st.write(container_client.get_container_properties())
            #st.subheader('Container Info ')
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(":key: <span style='color:blue;'>** Name **</span>", unsafe_allow_html = True)
            with col2:
                st.markdown(":computer: <span style='color:purple;'>** Last Modified **</span>", unsafe_allow_html = True)
            col1, col2 = st.columns(2)
            with col1:
                st.code(container_client.get_container_properties()['name'])
            with col2:
                st.code(container_client.get_container_properties()['last_modified'])
            
            #properties = blob_client.get_blob_properties()
            # [END upload_blob_to_container]

            # [START list_blobs_in_container]
            period = '.'
            slash = '/'
            tmp_list = container_client.list_blobs()
            blobs_list = ['Choose blob'] + list([x['name'] for x in tmp_list])
            for item in blobs_list.copy():
                if period in item or slash in item:
                    blobs_list.remove(item)
            if 'data_blob' not in st.session_state:
                st.session_state.data_blob = blobs_list[0]
            st.session_state.data_blob = st.selectbox('Blobs', blobs_list, index = blobs_list.index(st.session_state.data_blob))
            if st.session_state.data_blob == blobs_list[0] and len(blobs_list) != 1:

                st.error('Please choose a blob')
            else:
                if len(blobs_list) != 1 : 
                    blob_client = container_client.get_blob_client(blob = st.session_state.data_blob)
                    st.text(blob_client.get_blob_properties())
                #display container info
                container_client = st.session_state.blob_service_client.get_container_client(st.session_state.data_container)
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(":calendar: <span style='color:blue;'>** Creation Date **</span>", unsafe_allow_html = True)
                with col2:
                    st.markdown(":computer: <span style='color:purple;'>** Last Modified **</span>", unsafe_allow_html = True)
                col1, col2 = st.columns(2)
                with col1:
                    st.code(blob_client.get_blob_properties()['creation_time'])
                with col2:
                    st.code(blob_client.get_blob_properties()['last_modified'])

    #####################################################################
                now = datetime.datetime.now().strftime('%Y_%m_%d_%Hh%Mmn%Ss')
                # format selectbox
                formatlist = ['parquet', 'csv']
                if 'data_format' not in st.session_state:
                    st.session_state.data_format = 'parquet'
                st.session_state.data_format = st.selectbox('Destination files format', formatlist, index = formatlist.index(st.session_state.data_format))
                

                if st.button("Add data to Blob Azure"):
                    st.session_state.message = f"Loading ..."
                    st.session_state.success = st.success(st.session_state.message)
                    for i in range(num_files):
                        data = generate_utils.generate_data(num_lines)
                        
                        try : 
                            blob_client = st.session_state.blob_service_client.get_blob_client(container = st.session_state.data_container, blob=st.session_state.data_blob +'/'+st.session_state.data_format + '/chemical_elements_' + str(datetime.datetime.now()) + ".{}".format(st.session_state.data_format))
                            app_utils.upload_to_blob(blob_client,data,st.session_state.data_format)
                            st.session_state.message = f"File number {i} generated and added to Blob."
                            
                        except Exception as e: 
                            st.error(e)
                    #st.session_state.success = st.success(st.session_state.message)

            #         app_utils.upload_to_blob(blob_client,data,st.session_state.data_format)
            #         st.markdown(":file_folder: <span style='color:blue;'>** chemical_elements_" + str(now) + "**</span>", unsafe_allow_html = True)
            #         st.markdown("<span style='color:purple;'>** ______ uploaded to Azure Blob Stroage in " + st.session_state.data_blob +'/'+st.session_state.data_format + "**</span>", unsafe_allow_html = True)
            st.write("---")

