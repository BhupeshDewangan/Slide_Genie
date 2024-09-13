import streamlit as st
from src.helper import *
from src.download_files import *
from PIL import Image


def generate():
    st.title("Slide Genie - Text to PPT Generator Using Gemini")

    # Input box for text
    text = st.text_area("Enter the Topic for the PPT:")

    col1, col2 = st.columns(2)

    language = col1.selectbox(
        "Language",
        ("English", "Hindi"),
    )

    tone = col2.selectbox(
        "Tone",
        ("Casual", "Funny", "Professional", "Educational", "Sales Pitch"),

    )

    # Input box for number of slides
    num_slides = st.number_input("Enter the Number of Slides:", min_value=1, max_value=15, value=2)

    st.divider()

    st.success("You need to select a Template...")

    if 'template' not in st.session_state:
        st.session_state.template = ""

    with st.expander("Templates"):
        col1, col2 = st.columns(2)
        template1 = Image.open("Images/template1.png")
        template2 = Image.open("Images/template2.png")
        template1 = template1.resize((300, 200))
        template2 = template2.resize((300, 200))

        with col1:
            col1.image(template1)
            if col1.button("Select This"):
                st.session_state.template = "Templates/Template - 1.pptx"
                col1.write("Template 1 Selected")

        with col2:
            col2.image(template2)
            if col2.button('Select That'):
                st.session_state.template = "Templates/Template - 2.pptx"
                col2.write("Template 2 Selected")


    # Button to generate PPT
    if st.button("Generate PPT"):
        with st.spinner('Generating PPT... It may take A Minute'):

            presentation_data = get_synthetic_data(num_slides, text, language, tone)

            with open('JSON/presentation_data.json', 'w', encoding='utf-8') as f:
                f.write(presentation_data)

            automate_ppts(text, st.session_state.template)
            
            st.success("PPT generated successfully!")

            # Generate download links
            with st.expander("Download Links Are Here "):
                display_download_links(f"PPTs/{text}")


            # with st.expander("SHS"):
            #     show_pdf("PDFs/MAJOR PROJECT  SEM 8.pdf")

            # st.success("You Can Download PPT Here !!")

            # schedule.every(2).days.do(job)
