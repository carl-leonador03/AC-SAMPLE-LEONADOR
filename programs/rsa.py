from math import gcd
from random import choice

def mod_inverse(e: int, phi: int) -> int:
    """Modular Multiplicative Inverse function of `e mod phi(n)`.
    This function calculates the decryption key (or private key)."""
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
        
    return -1

def generate_keys(p: int, q: int) -> tuple[int, int, int]:
    """Key generator function for public and private keys.
    Returns a tuple of the public and private keys, as well as the product of primes."""
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    
    d = mod_inverse(e, phi)

    return e, d, n

def power(base: int, expo: int, m: int) -> int:
    """Power function used for encryption and decryption, following the formula:
    `base^expo mod m`"""
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def encrypt(message: int, key: int, n: int) -> int:
    """Encrypt macro function for `encrypt_message` function."""
    return power(message, key, n)

def decrypt(cipher: int, key: int, n: int) -> int:
    """Decrypt macro function for `decrypt_message` function."""
    return power(cipher, key, n)

def encrypt_message(message: str, key: int, n: int) -> list[int]:
    """Encrypts the plain text using public key."""
    encrypted = []
    for m in message:
        encrypted.append(encrypt(ord(m), key, n))
    
    return encrypted

def decrypt_message(cipher: list[int], key: int, n: int) -> list[int]:
    """Decrypts the cipher text using private key."""
    decrypted = []
    for c in cipher:
        decrypted.append(decrypt(c, key, n))
    
    return decrypted

def gen_primes() -> tuple[int, int]:
    """Function to generate random 3-digit prime numbers. For `p` and `q`."""
    primes = [i for i in range(100, 1000) if isPrime(i)]
    return choice(primes), choice(primes)

def isPrime(x: int) -> bool:
    """Checker function if `x` is a prime number or not."""
    return not any(x % i == 0 for i in range(2, x))