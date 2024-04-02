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


# st.latex(r'''
# a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# \sum_{k=0}^{n-1} ar^k =
# a \left(\frac{1-r^{n}}{1-r}\right)
# ''')

