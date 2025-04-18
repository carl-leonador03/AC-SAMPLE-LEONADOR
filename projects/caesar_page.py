import streamlit as st
import pandas as pd     # this is needed for st.tables apparently

from inspect import getmembers, isfunction, signature
from random import randint

# ------------ TO USE THE CODE FOR DEMO -------------
from programs import caesar as cs
# ------------ ------------------------ -------------

st.title("Caesar Cipher")
st.write("Activity 1 - 2/11/2025")

tab1, tab2, tab3 = st.tabs([":material/info: Description", ":material/code: Program Code", ":material/play_circle: Demonstration"])

tab1.write(
    "You are tasked with implementing a Python program that utilizes the Caesar Cipher technique to encrypt and decrypt a given text using multiple shift keys. The Caesar Cipher is a simple encryption method where each letter in the plaintext is shifted a certain number of places down the alphabet. The challenge is to extend this technique to support multiple shift keys for each character in the input text.")

tab1.write(
    "A function `encrypt_decrypt` that takes a text, a list of shift keys, and a boolean flag **ifdecrypt** as input parameters. The function iterates through each character in the text, applying the corresponding shift key based on the position in the text. The result is either encrypted or decrypted based on the value of the **ifdecrypt** flag.")

tab1.subheader("Constraints")
tab1.write("`accepted text chars(decimal(32-126))`")
tab1.write("`1 < Shift keys length <= len(text)`")

with tab2:
    st.header("Functions")
    
    tile = st.container(border = True)

    s = signature(cs.encrypt_decrypt)
    return_type = str(s.return_annotation)

    if "<class " in return_type:
        if "inspect._empty" in return_type:
            return_type = "None"
        else:
            return_type = return_type.replace("<class '", "")
            return_type = return_type.replace("'>", "")

    tile.markdown(f"###### {cs.encrypt_decrypt.__name__}: `{return_type}`")
    tile.markdown(f"{cs.encrypt_decrypt.__doc__.replace("\n", "\n\n") or ''}")
    tile.markdown("**Parameters**")
    tile.markdown("- ".join(
        [""] + [
            f"""`{x}` :blue-badge[{(
                str(s.parameters[x].annotation).replace("<class '", "").replace("'>", "") if "<class " in str(s.parameters[x].annotation) else str(s.parameters[x].annotation)
                )}]\n""" for x in s.parameters
        ]
    ))
            
    st.header("Source code")

    with open("programs/caesar.py", "r") as f:
        st.code(f.read())

if 'generate' not in st.session_state:
    st.session_state['generate'] = False

if 'shifts' not in st.session_state:
    st.session_state['shifts'] = ""

with tab3:
    if "shifts" not in st.session_state.keys():
        st.session_state['key_value'] = ""

    st.write("**Caesar Cipher demonstration**")
    plaintext = st.text_input("Plaintext", placeholder = "Insert plaintext here")

    shifts_con1, shifts_con2 = st.columns([80,17.5], vertical_alignment = "bottom")

    shifts_con2.button(":material/ifl: Generate", type = "primary", on_click = lambda: st.session_state.update({"shifts": " ".join([str(randint(-1000, 1000)) for _ in range(randint(1, 11))])}))

    shifts = shifts_con1.text_input("Character shifts", placeholder = "Integers separated by spaces", value = st.session_state['shifts'])

    demo = st.button("Encrypt and Decrypt", type = "primary")

    if demo:
        if plaintext == "" or (shifts == "" and st.session_state['shifts'] == ""):
            if plaintext == "":
                st.error(":material/error: Please enter your plaintext.")
            elif shifts == "":
                st.error(":material/error: Please enter character shifts for the cipher.")
            else:
                st.error(":material/error: Fields should not be empty.")
        else:
            with st.spinner("Processing...", show_time = True):
                res_enc = cs.encrypt_decrypt(
                    plaintext,
                    [int(x) for x in shifts.split(" ")] if not st.session_state['generate'] else [int(x) for x in st.session_state['shifts'].split(" ")],
                    False
                )

                res_dec = cs.encrypt_decrypt(
                    res_enc[0],
                    [int(x) for x in shifts.split(" ")] if not st.session_state['generate'] else [int(x) for x in st.session_state['shifts'].split(" ")],
                    True
                )
                
                st.write("**Output**")
                st.code(f"Text: \t\t{plaintext} \nShift keys: \t{" ".join(shifts.split(" ") if not st.session_state['generate'] else st.session_state['shifts'].split(" "))} \nCipher: \t{res_enc[0]} \nDecrypted text: {res_dec[0]}", language = "text")

                with st.expander("See the encryption and decryption tables"):
                    encryption = res_enc[1]
                    decryption = res_dec[1]

                    etab, dtab = st.columns(2)
                    
                    etab.subheader("Encryption")
                    etab.table(
                        pd.DataFrame(
                            {
                                "plaintext": [x[1] for x in encryption],
                                "shift": [f"`{x[2]}`" + (":material/arrow_downward:" if x[2] > 0 else ":material/arrow_upward:") for x in encryption],
                                "ciphertext": [x[3] for x in encryption]
                            }
                        )
                    )

                    dtab.subheader("Decryption")
                    dtab.table(
                        pd.DataFrame(
                            {
                                "ciphertext": [x[1] for x in decryption],
                                "shift": [f"`{x[2]}`" + (":material/arrow_upward:" if x[2] > 0 else ":material/arrow_downward:") for x in decryption],
                                "plaintext": [x[3] for x in decryption]
                            }
                        )
                    )