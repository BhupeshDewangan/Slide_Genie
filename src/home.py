import streamlit as st

def home():
    st.markdown('<h3 style= "text-align: center">Welcome to</h3>', unsafe_allow_html=True)
    st.markdown('<h1 style="color: #ff4b4b; text-align : center">Slide Genie</h1>', unsafe_allow_html=True)

    st.divider()
    st.header("About Slide Genie - A Text to PPT Generation Site")
    st.write(
        """
        **Slide Genie** is an innovative approach to creating presentation slides from textual content using **Gemini**. This cutting-edge technology leverages the power of artificial intelligence to automatically convert written text into professionally designed PowerPoint presentations.
        """)

    col1, col2 = st.columns(2)

    col1.header("Why Text to PPT?")
    col1.write(
        """
        - **Efficiency:** Save valuable time by automating the slide creation process. Instead of manually crafting each slide, you provide the text and let the AI handle the design and formatting.
        - **Consistency:** Ensure a uniform style and layout throughout your presentation. The model follows design principles to keep slides cohesive and visually appealing.
        - **Customization:** Tailor the output to fit specific themes or styles, making sure your presentations align with your branding or personal preferences.
        """)


    col2.header("How It Works")


    col2.write("""
        1. **Input Text:** You start by providing the content, language, tone, numbers of slides, template you want to include in your presentation.
        2. **AI Processing:** The Gemini processes this Input, understanding context, key points, and structure.
        3. **Slide Generation:** Then Using Python and Gemini generates slides with well-organized content, appropriate visuals with a Preloaded Template Design.
        4. **Review and Edit:** You have the option to review and make any adjustments to ensure the presentation meets your needs.
        """
    )

    st.header("Mission")
    st.write("At Slide Genie, our mission is to empower users with an efficient and intuitive way to create presentations. We strive to achieve this by leveraging cutting-edge AI technology and delivering a seamless user experience.")

    st.header("Development Tech and Tools")
    st.markdown("""
    - Python and Streamlit
    - Gemini 1.5-Flash Model
    - PPTX, JSON, Request
    """)

    st.header("Contact Me")

    st.write("I value your feedback and are always eager to hear from our users. If you have any questions, suggestions, or encounter any issues while using Slide Genie, please don't hesitate to reach out to us. You can contact us via:")

    st.markdown("""
    - Email : bhupeshdewangan2003@gmail.com
    - Phone : 8319341550
    - Linkedin : https://www.linkedin.com/in/bhupesh-dewangan-7121851ba/
    - Github : https://github.com/BhupeshDewangan
    """)

    st.error("If you come across any technical issues or bugs within the app, please report or send a message to me. Your input helps us improve Slide Genie and deliver a seamless experience for all users.")

    st.write("---")
    st.success("Thank you for choosing Slide Genie. We appreciate your support and look forward to serving you better in the future.")

    st.warning("Dive into a new era of presentation creation where AI turns your text into captivating slides. Experience the future of effortless and impactful presentations with Slide Genie!")
