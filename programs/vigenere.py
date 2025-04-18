def vigenere_encrypt(plaintext: str, key: str, alphabet: str) -> str:
    """
    Encrypts plaintext using a Vigenére cipher with custom alphabet.
    
    Args:
        plaintext: Input text containing only characters from the alphabet
        key: Key containing only characters from the alphabet
        alphabet: String of unique characters defining charcater order (index = value)
    
    Returns:
        Encrypted ciphertext string
    """

    # Check if alphabet contains duplicates
    if len(alphabet) != len(set(alphabet)):
        raise ValueError("Alphabet must contain unique characters")
    
    # Check if alphabet is empty
    if alphabet == "":
        raise ValueError("Alphabet cannot be empty")
    
    # Check if plaintext is empty
    if plaintext == "":
        raise ValueError("Plaintext cannot be empty")

    # Check if key is empty
    if key == "":
        raise ValueError("Key cannot be empty")
    
    # Checks if all characters in plaintext and/or key exists in the custom alphabet
    plaintext_invalid_chars = sorted({x for x in plaintext if x not in alphabet and x != " "})
    key_invalid_chars = sorted({x for x in key if x not in alphabet})

    if len(plaintext_invalid_chars) != 0 and len(key_invalid_chars) != 0:
        raise ValueError(f"Invalid characters!\nin plaintext: {', '.join(plaintext_invalid_chars)}\nin key: {', '.join(key_invalid_chars)}\nare not in alphabet")
    else:
        if len(plaintext_invalid_chars) > 0:
            raise ValueError(f"Invalid characters!\nin plaintext: {', '.join(plaintext_invalid_chars)}\n{'are' if len(plaintext_invalid_chars) > 1 else 'is'} not in alphabet")
        elif len(key_invalid_chars) > 0:
            raise ValueError(f"Invalid characters!\nin key: {', '.join(key_invalid_chars)}\n{'are' if len(key_invalid_chars) > 1 else 'is'} not in alphabet")
    
    # FINALLY, THE CIPHER!!!!!!!!!!!!
    cipher_text = []
    key_index = 0

    for plainchar in plaintext:
        if plainchar == " ":
            cipher_text.append(" ")
        else:
            plainchar_value = alphabet.index(plainchar)
            keychar_value = alphabet.index(key[key_index % len(key)])
            cipher_text.append(
                alphabet[(plainchar_value + keychar_value) % len(alphabet)]
            )
            key_index += 1

    return "".join(cipher_text)

if __name__ == '__main__':
    alphabet = input()
    plaintext = input()
    key = input()

    try:
        print("Encrypted:", vigenere_encrypt(plaintext, key, alphabet))
    except ValueError as err:
        print(err.__class__.__name__ + ":", str(err))
