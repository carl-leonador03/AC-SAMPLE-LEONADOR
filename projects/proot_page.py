import streamlit as slt
from inspect import getmembers, isfunction, signature
from random import choice

# ------------ TO USE THE CODE FOR DEMO -------------
from programs import proot as pr
# ------------ ------------------------ -------------

slt.title("Primitive Root")
slt.write("Activity 4 - 3/12/2025")

tab1, tab2, tab3 = slt.tabs([":material/info: Description", ":material/code: Program Code", ":material/play_circle: Demonstration"])

with tab1:
    slt.title("Primitive Root")
    
    slt.write("Find the Primitive roots of the given prime number **q** and check if the given primitive root **g** is a primitive root of **q**")

    slt.subheader("Inputs")
    slt.write("""
            `q` = prime number
            `g` = is the primitive root of q
              """)

    slt.subheader("Constraints")
    slt.write("**g < q")

    slt.subheader("Sample output")
    slt.code("""
            7 # input for q (prime number)
            5 # input for g (primitive root)
            1^1 mod 7 = 1,
            2^1 mod 7 = 2, 2^2 mod 7 = 4, 2^3 mod 7 = 1,
            3^1 mod 7 = 3, 3^2 mod 7 = 2, 3^3 mod 7 = 6, 3^4 mod 7 = 4, 3^5 mod 7 = 5, 3^6 mod 7 = 1 ==> 3 is primitive root of 7,
            4^1 mod 7 = 4, 4^2 mod 7 = 2, 4^3 mod 7 = 1,
            5^1 mod 7 = 5, 5^2 mod 7 = 4, 5^3 mod 7 = 6, 5^4 mod 7 = 2, 5^5 mod 7 = 3, 5^6 mod 7 = 1 ==> 5 is primitive root of 7,
            6^1 mod 7 = 6, 6^2 mod 7 = 1,
            5 is primitive root: True [3, 5] 
            """)

with tab2:
    slt.header("Functions")
    
    pr_functions = getmembers(pr, isfunction)

    for i in range(0, len(pr_functions), 3):
        row = slt.columns(3)

        for j, col in enumerate(row):
            tile = col.container(border = True)

            s = signature(pr_functions[i+j][1])
            return_type = str(s.return_annotation)

            if "<class " in return_type:
                if "inspect._empty" in return_type:
                    return_type = "None"
                else:
                    return_type = return_type.replace("<class '", "")
                    return_type = return_type.replace("'>", "")

            tile.markdown(f"###### {pr_functions[i+j][0]}: `{return_type}`")
            tile.write(pr_functions[i+j][1].__doc__.replace("\n", "\n\n") if pr_functions[i+j][1].__doc__ != None else "")
            tile.markdown("**Parameters**")
            tile.markdown("- ".join(
                [""] + [
                    f"""`{x}` :blue-badge[{(
                        str(s.parameters[x].annotation).replace("<class '", "").replace("'>", "") if "<class" in str(s.parameters[x].annotation) else str(s.parameters[x].annotation)
                        )}]\n""" for x in s.parameters
                ]
            ))
            
    slt.header("Source code")

    with open("programs/proot.py", "r") as f:
        slt.code(f.read())

with tab3:
    slt.write("Prime root calculator")
    slt.caption(":material/info: Please do note that this system works well with small prime numbers. If a large prime number is entered, a `RuntimeError` may occur due to timeout issues or memory constraints.")
    g = slt.text_input("Input `g` value", help = "Input the number to check if it is a primitive root of `q`.")
    q = slt.text_input("Input `q` value", help = "Input a valid prime number")

    process = slt.button(":material/play_circle: Calculate", type = "primary")

    if process:
        try:
            slt.write(f"**Output:** \n `{pr.main(int(g), int(q))}`")
        except Exception as err:
            slt.error(str(err), icon = ":material/error:")
