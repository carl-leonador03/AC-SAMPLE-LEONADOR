import streamlit as st

st.set_page_config(
    page_title = "Applied Cryptography",
    page_icon = ":material/code_blocks:",
    layout = "wide"
)

pages = {
    "": [
        st.Page("home.py", title = "Home", icon = ":material/home:")
    ]
    ,
    "My projects": [
        st.Page("projects/caesar_page.py", title = "Caesar Cipher"),
        st.Page("projects/vigenere_page.py", title = "Vigenére Cipher"),
        st.Page("projects/block_page.py", title = "Block Cipher"),
        st.Page("projects/rsa_page.py", title = "RSA Algorithm"),
    ]
}

pg = st.navigation(pages)
st.logo("https://avatars.githubusercontent.com/u/178447516")

pg.run()