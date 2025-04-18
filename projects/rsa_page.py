import streamlit as st
from time import sleep

from inspect import getmembers, isfunction, signature
from programs import rsa

st.title("Rivest-Shamir-Adleman (RSA) Algorithm")

tab1, tab2, tab3 = st.tabs([":material/info: Description", ":material/code: Program Code", ":material/play_circle: Demonstration"])

# ------------------------------ [ Program Code ] ------------------------------------
with tab2:
    st.header("Functions")
    
    rsa_functions = getmembers(rsa, isfunction)

    for i in range(0, len(rsa_functions), 3):
        row = st.columns(3)

        for j, col in enumerate(row):
            tile = col.container(border = True)

            s = signature(rsa_functions[i+j][1])
            return_type = str(s.return_annotation)

            if "<class " in return_type:
                if "inspect._empty" in return_type:
                    return_type = "None"
                else:
                    return_type = return_type.replace("<class '", "")
                    return_type = return_type.replace("'>", "")

            tile.markdown(f"###### {rsa_functions[i+j][0]}: `{return_type}`")
            tile.write(rsa_functions[i+j][1].__doc__.replace("\n", "\n\n") or "")
            tile.markdown("**Parameters**")
            tile.markdown("- ".join(
                [""] + [
                    f"""`{x}` :blue-badge[{(
                        str(s.parameters[x].annotation).replace("<class '", "").replace("'>", "") if "<class" in str(s.parameters[x].annotation) else str(s.parameters[x].annotation)
                        )}]\n""" for x in s.parameters
                ]
            ))
            
    st.header("Source code")

    with open("programs/rsa.py", "r") as f:
        st.code(f.read())

# ------------------------------ [ Demonstration ] ------------------------------------
with tab3:
    st.write("RSA cipher algorithm demonstration")
    st.caption("Note: The demonstration generates two 3-digit prime numbers by random.")
    
    col1, col2 = st.columns(2, border = True)

    with col1:
        st.subheader("Alice")

        chatA_container, statusA_container = st.container(border = True), st.empty()

        with chatA_container:
            textspaceA, buttonspaceA = st.columns([9,1], vertical_alignment = "bottom")
            message = textspaceA.text_input("Send message to Bob:", placeholder = "Compose message")
            send = buttonspaceA.button(":material/send:", type = "primary")

        if send:
            if message == '':
                st.error("Empty message. Please enter something in the chat box.")
            else:
                statusA_container = st.expander(":material/lock: Encryption")

                p, q = rsa.gen_primes()
                e, d, n = rsa.generate_keys(p, q)
                encrypted_text = rsa.encrypt_message(message, e, n)

                statusA_container.markdown(
                    f"plaintext:\n\n`{message}`"
                )

                statusA_container.markdown(
                    f"plaintext array:\n\n`{" ".join([str(ord(x)) for x in message])}`"
                )

                statusA_container.markdown(
                    f"public key: `{str(p)}`"
                )

                statusA_container.markdown(
                    f"encrypted data:\n\n`{" ".join([str(x) for x in encrypted_text])}`"
                )
    
    with col2:
        st.subheader("Bob")

        chatB_container, statusB_container = st.container(border = True), st.empty()

        with chatB_container:
            chat_status = st.empty()
        
        if not send:
            with chat_status:
                st.caption("No new messages.")

        if send:
            if message != '':
                chatB_container = st.container(border = True)
                statusB_container = st.expander(":material/lock_open_right: Decryption")

                with chatB_container:
                    with chat_status:
                        st.badge(":material/mark_email_unread: New message from Alice", color = "orange")

                with st.spinner("Receiving message..."):
                    decrypted_text = rsa.decrypt_message(encrypted_text, d, n)
                    sleep(2.5)

                    with chat_status:
                        st.markdown(f":blue-badge[**ALICE**]: {"".join([chr(x) for x in decrypted_text])}")

                    statusB_container.markdown(
                        f"received data:\n\n`{" ".join([str(x) for x in encrypted_text])}`"
                    )

                    statusB_container.markdown(
                        f"private key: `{str(d)}`"
                    )

                    statusB_container.markdown(
                        f"decrypted data array:\n\n`{" ".join([str(x) for x in decrypted_text])}`"
                    )

                    statusB_container.markdown(
                        f"decrypted text:\n\n`{"".join([chr(x) for x in decrypted_text])}`"
                    )

            else:
                with chat_status:
                    st.caption("No new messages.")