import hashlib
from sympy import randprime

def rsa_key_generation():
    p = randprime(2**255,2**256)
    q = randprime(2**255,2**256)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def sign_message(message, private_key):
    d, n = private_key
    hash_hex = hashlib.sha256(message.encode()).hexdigest()
    hash_int = int(hash_hex,16)
    signature = pow(hash_int, d, n)
    return hash_hex, signature

def verify_signature(message, signature, public_key):
    e, n = public_key
    hash_hex = hashlib.sha256(message.encode()).hexdigest()
    hash_int = int(hash_hex,16)
    decrypted = pow(signature, e, n)
    return decrypted == hash_int


public_key, private_key = rsa_key_generation()

message = input("\nEnter the message to sign: ")
h1, s1 = sign_message(message, private_key)
print(f"Hash (H1): {h1}")
print(f"Signature (S1): {s1}")

message_to_verify = input("\nEnter the message to verify: ")
signature_input = int(input("Enter the signature to verify: "))

if verify_signature(message_to_verify, signature_input, public_key):
    print("\nVerification successful")
else:
    print("\nVerification failed")
