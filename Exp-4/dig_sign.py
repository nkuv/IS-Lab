import hashlib
import secrets
import math

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    # Write n-1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = secrets.randbelow(n-3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        candidate = secrets.randbits(bits)
        candidate |= (1 << (bits - 1))  # Ensure high bit is set
        candidate |= 1  # Ensure odd
        if miller_rabin(candidate):
            return candidate

def rsa_key_generation():
    p = generate_prime(129)
    q = generate_prime(129)
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    while math.gcd(e, phi) != 1:
        e += 2
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def sign_message(message, private_key):
    d, n = private_key
    hash_bytes = hashlib.sha256(message.encode()).digest()
    hash_int = int.from_bytes(hash_bytes, byteorder='big')
    signature = pow(hash_int, d, n)
    return hash_bytes.hex(), signature

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