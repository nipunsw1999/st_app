import streamlit as st 
from streamlit_option_menu import option_menu
from langchain_app import name

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options = ["Home","Chatbot","Projects","Contact","About"],
        icons = ["house-door","robot","gear","telephone","asterisk"],
        menu_icon = "list",
        default_index = 0,
    )

if selected:
    st.title(f"You selected {selected}")


st.title(name)