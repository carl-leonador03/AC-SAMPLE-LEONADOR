import streamlit as st

st.title("your stove was left running")
st.write(
    "yeah check your stove. gas leak"
)

tab1, tab2, tab3 = st.tabs(["Details", "Related", "Files"])

tab1.write("a landmine was secretly installed at an undisclosed area within your home :)")

tab2.write("something something literally 1984 something")

tab3.write("sorry i ate them :(")