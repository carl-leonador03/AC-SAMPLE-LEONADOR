import streamlit as st

from inspect import getmembers, isfunction, signature

# ------------ TO USE THE CODE FOR DEMO -------------
from programs import vigenere as vgn
# ------------ ------------------------ -------------

st.title("Vigenére Cipher")
st.write("Activity 2 - 2/18/2025")

tab1, tab2, tab3 = st.tabs([":material/info: Description", ":material/code: Program Code", ":material/play_circle: Demonstration"])

with tab1:
    st.markdown(
        """
        ## Dynamic Alphabet Vigenére
        
        ### Problem Description
        Implement a Vigenére cipher with these strict requirements:
        - **Custom Alphabet:**
            - Must contain unique characters (no duplicates)
            - Minimum length: 1 character
            - Defines character values (index = value)
        - **Inpyt Validation:**
            - Plaintext and key must only contain characters from the alphabet
            - Reports all invalid characters in both plaintext and key
            - Error format: "Invalid characters: not in alphabet"
        - **Key Handling:**
            - Repeated cyclically to match plaintext string
            - Cannot be empty string
        - **Cipher Operation:**
            - `ciphertext_char = (plaintext_char_value + key_char_value) % alphabet_length`
        """
    )

    st.subheader("Sample Input/Output")

    con = st.container(border = True)

    with con:
        st.markdown("**Custom Alphabet:** `ZYXWVUTSRQPONMLKJIHGFEDCBA`")
        st.markdown("**Plaintext:** `HELLO`")
        st.markdown("**Key:** `KEY`")
        st.markdown("**Valid Output:** `SJKWT`")
        st.markdown("**Invalid Example:**")
        st.markdown("**Alphabet:** `ABCD`")
        st.markdown("**Plaintext:** `HELLO`")
        st.markdown("**Key:** `KEY`")
        st.markdown("**Output:**")
        st.code(
            """ValueError: Invalid characters!
in plaintext: E, H, L, O
in key: E, K, Y
are not in alphabet"""
        )

with tab2:
    st.header("Functions")
    
    tile = st.container(border = True)

    s = signature(vgn.vigenere_encrypt)
    return_type = str(s.return_annotation)

    if "<class " in return_type:
        if "inspect._empty" in return_type:
            return_type = "None"
        else:
            return_type = return_type.replace("<class '", "")
            return_type = return_type.replace("'>", "")

    tile.markdown(f"###### {vgn.vigenere_encrypt.__name__}: `{return_type}`")
    tile.markdown(f"{vgn.vigenere_encrypt.__doc__.replace("\n", "\n\n") or ''}")
    tile.markdown("**Parameters**")
    tile.markdown("- ".join(
        [""] + [
            f"""`{x}` :blue-badge[{(
                str(s.parameters[x].annotation).replace("<class '", "").replace("'>", "") if "<class " in str(s.parameters[x].annotation) else str(s.parameters[x].annotation)
                )}]\n""" for x in s.parameters
        ]
    ))
            
    st.header("Source code")

    with open("programs/vigenere.py", "r") as f:
        st.code(f.read())

with tab3:
    st.write("Vigenére Cipher demonstration")

    alphabet = st.text_input("Alphabet", placeholder = "Insert unique characters to encrypt and decrypt from")
    plaintext = st.text_input("Plaintext", placeholder = "Insert a normal text message")
    key = st.text_input("Key", placeholder = "Insert a key string for encryption", help = "Unless spaces are included in your alphabet, key should contain no spaces.")

    button = st.button("Encrypt", type = "primary", icon = ":material/lock:")
    result = st.empty()

    if button:
        try:
            encrypted = vgn.vigenere_encrypt(plaintext, key, alphabet)

            result.write(f"**Result:** `{"".join(encrypted)}`")
        except ValueError as err:
            st.error(f"**{err.__class__.__name__}:**\n{(str(err)) if "\n" not in str(err) else str(err).replace("\n", "\n\n")}", icon = ":material/error:")