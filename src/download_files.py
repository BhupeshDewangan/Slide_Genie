import streamlit as st
import os
import json
import base64
from io import BytesIO
from urllib.request import urlopen
from pptx import Presentation




def generate_download_links(folder_name):
    """
    Generate download links for all PPT files in the specified folder.
    """
    links = []
    
    # Ensure the directory exists
    if not os.path.exists(folder_name):
        st.error(f"The directory {folder_name} does not exist.")
        return links

    # List all .pptx files in the folder
    ppt_files = [f for f in os.listdir(folder_name) if f.endswith('.pptx')]

    for ppt_file in ppt_files:
        file_path = os.path.join(folder_name, ppt_file)
        
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            href = f'<a href="data:application/vnd.openxmlformats-officedocument.presentationml.presentation;base64,{b64}" download="{ppt_file}">Download {ppt_file}</a>'
            links.append(href)

    return links


def display_download_links(folder_name):
    """
    Display download links for all PPT files in the specified folder using Streamlit.
    """
    links = generate_download_links(folder_name)
    
    if links:
        for link in links:
            st.markdown(link, unsafe_allow_html=True)
    else:
        st.info("No PowerPoint files found in the specified folder.")
