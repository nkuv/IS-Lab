import hashlib
import sympy 
import math

# Function to generate a 256-bit prime using sympy
def generate_prime(bits=256):
    # Define the range for a 256-bit number
    lower_bound = 2**(bits - 1)
    upper_bound = 2**bits - 1
    
    # Generate a random prime number within this range using sympy's randprime
    prime = sympy.randprime(lower_bound, upper_bound)
    return prime

# RSA key generation with 256-bit prime
def rsa_key_generation():
    p = generate_prime(128)  # Generate a 256-bit prime for p
    q = generate_prime(128)  # Generate a 256-bit prime for q
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while math.gcd(e, phi) != 1:
        e += 2
    d = pow(e, -1, phi)
    return (e, n), (d, n)

# Signing the message
def sign_message(message, private_key):
    d, n = private_key
    hash_bytes = hashlib.sha256(message.encode()).digest()
    hash_int = int.from_bytes(hash_bytes, byteorder='big')
    signature = pow(hash_int, d, n)
    return hash_bytes.hex(), signature

# Verifying the signature
def verify_signature(message, signature, public_key):
    e, n = public_key
    hash_bytes = hashlib.sha256(message.encode()).digest()
    hash_int = int.from_bytes(hash_bytes, byteorder='big')
    decrypted = pow(signature, e, n)
    return decrypted == hash_int

# Key Generation
public_key, private_key = rsa_key_generation()
print("Public key (e, n):", public_key)

# Signing
message = input("\nEnter the message to sign: ")
h1, s1 = sign_message(message, private_key)
print(f"Hash (H1): {h1}")
print(f"Signature (S1): {s1}")

# Verification
message_to_verify = input("\nEnter the message to verify: ")
e_input = int(input("Enter public key e: "))
n_input = int(input("Enter public key n: "))
public_key_input = (e_input, n_input)
s1_input = int(input("Enter the signature to verify: "))

# Compute H2 and S2
h2 = hashlib.sha256(message_to_verify.encode()).hexdigest()
s2 = pow(s1_input, public_key_input[0], public_key_input[1])
s2_bytes = s2.to_bytes(32, byteorder='big')  # SHA-256 produces 32 bytes
s2_hex = s2_bytes.hex()

print(f"Decrypted Signature (S2): {s2_hex}")
print(f"Recomputed Hash (H2): {h2}")

if verify_signature(message_to_verify, s1_input, public_key_input):
    print("Verification successful")
else:
    print("Verification failed")
