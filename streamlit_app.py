import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write(
    "Once again, Germany took a huge L on this war."
)
st.write(
    "Adolf thought fr fr 💀"
)
st.write(
    "However, bro got cooked by British Forces."
)
st.write(
    "W in the chat, for United Kingdom."
)
st.html(
    "<i>- Winston Churchill</i>"
)
st.divider()
button = st.button("Send W in chat")

if button:
    print("W")
    