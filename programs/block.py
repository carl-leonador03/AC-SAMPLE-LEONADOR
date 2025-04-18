def encrypt(plaintext: str, key: str) -> list[str]:
    """Encrypts plaintext with an 8 characters long key using ECB mode.

    Returns the encrypted ciphertext.
    Raises `ValueError` if key is not exactly 8 characters long."""

    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters")

    blocks = [plaintext[i : i + 8] for i in range(0, len(plaintext), 8)]
    cipher = []

    # Append "_" to last item if len(x) < 8
    if len(blocks[-1]) < 8:
        blocks[-1] = blocks[-1] + ("_" * (8 - len(blocks[-1])))
    
    for block in blocks:
        for c, k in zip(block, key):
            cipher.append(format(ord(c) ^ ord(k), "x").zfill(2).upper())
    
    # Return the ciphertext
    return cipher

def decrypt(ciphertext: list[hex], key: str) -> str:
    """Decrypts an array of *assumed* encrypted data with its
    8 character long key using ECB mode.
    
    Returns the decrypted plaintext.
    Raises `ValueError` if key is not exactly 8 characters long."""

    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters")
    
    blocks = [ciphertext[i : i + 8] for i in range(0, len(ciphertext), 8)]
    plain = []

    for block in blocks:
        # Check if ciphertext isn't in multiples of 8 ('_' were somehow disregarded)
        if len(block) == 8:
            # Good. its in muliples of 8
            for c, k in zip(block, key):
                plain.append(chr(c ^ ord(k)))
        
        else:
            # Uhh what happened...
            # Welp, ig we'll just pad it off with zeroes and disregard them laten then.
            for c, k in zip(block + ([0x0] * (8 - len(block))), key):
                if c != 0x0:
                    plain.append(chr(c ^ ord(k)))
    
    # Disregard the padding on return :)
    return "".join([x for x in plain if x != "_"])

def main(inp_str: str, key_str: str, mode: str) -> list[int] | str:
    if mode.lower() not in ["encrypt", "decrypt"]:
        raise ValueError("Invalid operation. Use 'encrypt' or 'decrypt'")
    
    else:
        if mode.lower() == "encrypt":
            # Check if input is valid
            if all(32 <= ord(x) < 126 for x in inp_str):
                return " ".join(encrypt(inp_str, key_str))
            
            else:
                raise ValueError("Invalid characters in plaintext")
        
        elif mode.lower() == "decrypt":
            # Check if input is valid, assuming its a series of hex values
            hex_array = (
                inp_str.split(" ") # Split them if it was separated by spaces (hopefully)
                if " " in inp_str
                else [inp_str[i : i + 2] for i in range(0, len(inp_str), 2)]
                # Split them by two because it wasn't separated by spaces :(
            )

            try:
                return decrypt([int(x, 16) for x in hex_array], key_str)
            
            except ValueError:
                raise ValueError("Malformed hex data entered")

if __name__ == '__main__':
    x = input()
    y = input()
    z = input()
    try:
        main(x, y, z)
    
    except Exception as err:
        print("Error:", err)