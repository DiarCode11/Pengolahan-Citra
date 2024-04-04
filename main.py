import streamlit as st

st.set_page_config(
    page_title="Web Team 2",
    page_icon="🗿",
)

# Ini buat ngasih title
st.title("Web Team 2")

# Menu pertama
st.sidebar.header("Menu 1")
st.sidebar.subheader("Submenu 1.1")
st.sidebar.subheader("Submenu 1.2")

# Menu kedua
st.sidebar.header("Menu 2")
st.sidebar.subheader("Submenu 2.1")
st.sidebar.subheader("Submenu 2.2")

st.sidebar.success("Pilih fitur di atas")


