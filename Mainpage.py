import streamlit as st
from streamlit_scroll_navigation import scroll_navbar
from constant import *

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide", initial_sidebar_state="auto")

st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)
margin_r,body,margin_l = st.columns([0.1, 3, 0.2])

#sidebar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
anchor_ids = ["About", "Experience", "Skills"]
anchor_icons = ["info-circle", "laptop", "hammer"]

with st.sidebar:
    scroll_navbar(
        anchor_ids,
        anchor_labels=None, # Use anchor_ids as labels
        anchor_icons=anchor_icons)

with body:
    #main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.header("About Me",divider='rainbow', anchor='About')

    col1, col2, col3 = st.columns([1.3 ,0.2, 1])

    with col1:
        st.write(info['brief'])
        st.markdown(f"###### Name: {info['name']}")
        # st.markdown(f"###### Study: {info['study']}")
        st.markdown(f"###### Location: {info['location']}")
        st.markdown("[![Linkedin](http://raw.githubusercontent.com/kinwong-ds/streamlit-porfolio-v1/refs/heads/main/src/icons8-git-50.png)](https://github.com/kinwong-ds) [![Linkedin](http://raw.githubusercontent.com/kinwong-ds/streamlit-porfolio-v1/refs/heads/main/src/icons8-linkedin-50.png)](https://www.linkedin.com/in/ki-wong/)", unsafe_allow_html=True)


        
        with open("src/resume.pdf", "rb") as file:
            pdf_file = file.read()

        st.download_button(
            label="Download my :blue[resume]",
            data=pdf_file,
            file_name="resume",
            mime="application/pdf")

    with col3:
        st.image("src/portrait.jpeg", width=360)
    st.write('')
    st.write('')

    # Work Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.header("Experience",divider='rainbow', anchor='Experience')
    st.write("")

    def experience_unit(company, position, date, location, content,button_name,button_link):
        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            st.subheader(company)
        with col3:
            st.write("")
            st.markdown("#####   " + date)

        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            st.markdown("##### " + position)
        with col3:
            st.markdown("#####   " + location)

        st.write(content)
        st.link_button(button_name, button_link)
        st.divider()

    for exp in Experience:
        experience_unit(exp[0],exp[1],exp[2],exp[3],exp[4],exp[5],exp[6])

    # skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("My :blue[skills] ⚒️",divider='rainbow', anchor='Skills') 

    def skill_tab():
        rows,cols = len(info['skills'])//skill_col_size, skill_col_size
        skills = iter(info['skills'])
        if len(info['skills'])%skill_col_size!=0:
            rows+=1
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    columns[index_].button(next(skills))
                except:
                    break
    with st.spinner(text="Loading section..."):
        skill_tab()

    # Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

