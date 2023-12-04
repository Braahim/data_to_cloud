import streamlit as st 
import os
#import utils.app_utils as app_utils
from section import generation, parquet_viewer, about, azure_connect


st.set_page_config(page_title= "Generation App", page_icon= "chart_with_upwards_trend")


class multipage:  
    def __init__(self):
        self.pages = []
    def add_page(self,title,func): 
        self.pages.append({
            'title': title,
            'function': func 
        })  
    def run(self):  
        page = st.sidebar.radio(
            'Menu',
            self.pages, 
            format_func = lambda page : page['title'])
        st.session_state.app_pagename = page['title']
        page['function']()
 
page = multipage() 



################################################################################
###################### SETUP : BEGINNING #######################################
################################################################################
# sidebar titles management
st.sidebar.title('The APP')
# add all your application here
page.add_page('About the app', about.page)
page.add_page('Excel Generator', generation.page)
page.add_page('Parquet Viewer', parquet_viewer.page)
page.add_page('Connect to Azure', azure_connect.page)

 

  
# general path management
st.session_state.path_root = os.getcwd()
st.session_state.path_this = os.path.dirname(os.path.realpath(__file__))
st.session_state.path_data = '/'.join(st.session_state.path_this.split('/')[:-1])
# the main app  
page.run()

################################################################################
###################### SETUP : ENDING ##########################################
################################################################################ 


