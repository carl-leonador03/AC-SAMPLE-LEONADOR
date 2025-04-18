def encrypt_decrypt(text: str, shift_keys: list[int], ifdecrypt: bool) -> str:
    """
    Encrypts a text using Caesar Cipher with a list of shift keys.
    Args:
        text: The text to encrypt.
        shift_keys: A list of integers representing the shift values for each character.
        ifdecrypt: flag if decrypt or encrypt
    Returns:
        A string containing the encrypted text if encrypt and plaint text if decrypt
    """

    if len(shift_keys) < 1:
        raise ValueError("'shifted_keys' must have at least one integer to shift from.")
    
    chars = [x for x in range(32, 126)]
    shifted_keys = []

    # This is for encryption and decryption table. Not needed for the algorithm itself.
    shifted_keys_ = []

    for i, char in enumerate(text):
        index = chars.index(ord(char))

        if ifdecrypt:
            shifted_index = index - shift_keys[i % len(shift_keys)]
        else:
            shifted_index = index + shift_keys[i % len(shift_keys)]
        
        shifted_char = chr(chars[shifted_index % len(chars)])

        shifted_keys_.append((i, char, shift_keys[i % len(shift_keys)], shifted_char))

        shifted_keys.append(shifted_char)
    

    return ("".join(shifted_keys), shifted_keys_)

if __name__ == '__main__':
    text = input()
    shift_inputs = input()
    shift_keys = [int(x) for x in shift_inputs.split(" ")]
    cipher_text, c_table = encrypt_decrypt(text, shift_keys, False)
    decrypted_text, p_table = encrypt_decrypt(cipher_text, shift_keys, True)

    for c in c_table:
        print(*c)
    
    for p in p_table:
        print(*p)

    print("Text:", text)
    print("Shift keys:", " ".join([str(x) for x in shift_keys]))
    print("Cipher:", cipher_text)
    print("Decrypted text:", decrypted_text)