import streamlit as st
from src.home import *
from src.generator import *


st.set_page_config(page_title="Slide Genie", page_icon="✨", layout="wide", initial_sidebar_state="auto", menu_items=None)


def main():
    # Set up the sidebar
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Select a page:", ["Home", "Generate"])

    # Home page
    if page == "Home":
        home()

    # Generate page
    elif page == "Generate":
        generate()
    

if __name__ == "__main__":
    main()