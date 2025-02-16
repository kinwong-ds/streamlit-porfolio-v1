import streamlit as st
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Experience", page_icon="📚", layout="wide", initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
    # menu()

    st.header("Experience",divider='rainbow')
    st.write("")

    def experience_unit(company, position, date, location, content,button_name,button_link):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(company)
        with col3:
            st.write("")
            st.markdown("#####   " + date)

        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown("##### " + position)
        with col3:
            st.markdown("#####   " + location)

        st.write(content)
        st.link_button(button_name, button_link)
        st.divider()

    for exp in Experience:
        experience_unit(exp[0],exp[1],exp[2],exp[3],exp[4],exp[5],exp[6])



