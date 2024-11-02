import streamlit as st
from streamlit_navigation_bar import st_navbar as navbar

st.set_page_config(initial_sidebar_state="collapsed")

pages = ['Home', 'Yaici', 'MAKAKI', 'Zaulpi']

styles = {
    "nav": {
        "background-color": "rgb(135,172,35",
    },
    "div" : {
        "max-width":"32rem",
    },
    "span" : {
        "border-radius" : "0.5rem",
        "color":"rgb(15,120,85",
        "margin":"0 0.125rem",
        "padding" : "0.4375rem 0.625rem",
    },
    "active" : {
        "background-color" : "rgba(45,35,255,0.65",
    },
    "hover": {
        "background-color" : "rgba(175,175,175,0.75",
    }
}

page = navbar (pages, styles=styles)

if page == 'Home':
    Home.Home().app()
elif page == 'Yaici':
    Yaici.Yaici().app()
elif page == 'MAKAKI':
    MAKAKI.MAKAKI().app()
elif page == 'Zaulpi':
    Zaulpi.Zaulpi().app()
else:
    Home.Home().app()


