import streamlit as slt
from inspect import getmembers, isfunction, signature
from random import choice

# ------------ TO USE THE CODE FOR DEMO -------------
from programs import block as blk
# ------------ ------------------------ -------------

slt.title("Block Cipher")
slt.write("Activity 3 - 2/25/2025")

tab1, tab2, tab3 = slt.tabs([":material/info: Description", ":material/code: Program Code", ":material/play_circle: Demonstration"])

with tab1:
    slt.title("Block Cipher Learning Task")
    slt.subheader("Problem Definition")
    slt.write("Implement a simplified block cipher system that can encrypt and decrypt messages using Electronic Codebook (ECB) mode with the following requirements:")

    slt.subheader("Explanation")
    slt.markdown("""
                 The cipher should:
                 - Use 8-byte (64-bit) blocks
                 - Pad messages with '_' to them multiples of 8 bytes, else return (Error: Key must be exactly 8 characters)
                 - Use XOR operation with a repeating key for "encryption"
                 - Work for both encryption and decryption (since XOR is reversible)
                 - Use only 'encrypt' or 'decrypt' operation, else return (Error: Invalid operation. Use 'encrypt' or 'decrypt')""")
    
    slt.subheader("Constraints")
    slt.markdown("""
                 - Block size is fixed at 8 bytes
                 - Key must be exactly 8 ASCII characters
                 - Input text can only contain ASCII printable characters (32-126)
                 - Padding character is '_' (underscore)""")
    
    slt.subheader("Sample Input/Output")
    slt.markdown("""
                 **Input:**
                 ```
                 Hello
                 ABCDEFGH
                 encrypt
                 ```
                 
                 **Output:**
                 ```
                 09 27 2F 28 2A 19 18 17
                 ```""")
    
    slt.subheader("Test Cases")
    slt.markdown("""
                 | # | Text | Key | Operation | Expected Output |
                 | :- | :------------ | :---------- | :----------- | :-------------------- |
                 | 1 | "Hello" | "ABCDEFGH" | encrypt | `09 27 2F 28 2A 19 18 17` |
                 | 2 | "12345678" | "KEYKEYLE" | encrypt | `7A 77 6A 7F 70 6F 7C 7D` |
                 | 3 | "Data" | "12345678" | encrypt | `75 53 47 55 6A 69 68 67` |
                 | 4 | "Secret!!" | "!@#$%^&*" | encrypt | `72 25 40 56 40 2A 07 0B` |
                 | 5 | `11 60 46 48 18 53 19 64 33 29 54 4C 12 42 52 2D 23 60 45 04 04 49 1F 29 35 34 56 4D 14 1D 19 21 29 60 41 4A 14 42 0B 34 24 29 4B 4A 57 5D 17 30 38 2F 40 04 03 58 13 30 70 30 56 4B 14 55 01 37 35 33 04 42 1E 48 17 20 7D 2C 41 4A 10 44 1A 64 32 2C 4B 47 1C 43 52 2B 36 60 54 48 16 59 1C 30 35 38 50 04 13 51 06 25 70 29 4A 50 18 10 17 2A 33 32 5D 54 03 55 16 64 33 29 54 4C 12 42 06 21 28 34 04 46 1B 5F 11 2F 23 60 4B 42 57 44 1A 21 70 33 45 49 12 10 1E 21 3E 27 50 4C 59 6F 2D 1B` | "P@$$w0rD" | decrypt | A block cipher is a symmetric-key encryption method that processes fixed-length blocks of plaintext data into encrypted ciphertext blocks of the same length. |
                 """)
    
with tab2:
    slt.header("Functions")
    
    blk_functions = getmembers(blk, isfunction)

    for i in range(0, len(blk_functions), 3):
        row = slt.columns(3)

        for j, col in enumerate(row):
            tile = col.container(border = True)

            s = signature(blk_functions[i+j][1])
            return_type = str(s.return_annotation)

            if "<class " in return_type:
                if "inspect._empty" in return_type:
                    return_type = "None"
                else:
                    return_type = return_type.replace("<class '", "")
                    return_type = return_type.replace("'>", "")

            tile.markdown(f"###### {blk_functions[i+j][0]}: `{return_type}`")
            tile.write(blk_functions[i+j][1].__doc__.replace("\n", "\n\n") if blk_functions[i+j][1].__doc__ != None else "")
            tile.markdown("**Parameters**")
            tile.markdown("- ".join(
                [""] + [
                    f"""`{x}` :blue-badge[{(
                        str(s.parameters[x].annotation).replace("<class '", "").replace("'>", "") if "<class" in str(s.parameters[x].annotation) else str(s.parameters[x].annotation)
                        )}]\n""" for x in s.parameters
                ]
            ))
            
    slt.header("Source code")

    with open("programs/block.py", "r") as f:
        slt.code(f.read())

with tab3:
    if "key_value" not in slt.session_state.keys():
        slt.session_state['key_value'] = ""

    plaintext = slt.text_input("Plaintext input")
    key_ = slt.text_input("Key string", max_chars = 8, help = "Must be exactly 8 characters!", value = slt.session_state['key_value'], on_change = lambda: slt.session_state.update({"key_value": key_}))
    mode = slt.selectbox("Mode", ["encrypt", "decrypt"], format_func = lambda x: "Encrypt" if x == "encrypt" else "Decrypt")

    slt.button(":material/ifl: Random key string", on_click = lambda: slt.session_state.update({"key_value": "".join([choice([x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"]) for _ in range(8)])}))

    process = slt.button(":material/play_circle: Process", type = "primary")

    if process:
        try:
            slt.write(f"**Output:** \n `{blk.main(plaintext, key_, mode)}`")
        except Exception as err:
            slt.error(f"**Error:** {str(err)}", icon = ":material/error:")