from sympy import mod_inverse, gcd

def generate_keys():
    # Choose two distinct prime numbers
    p = int(input("Enter p value: "))
    q = int(input("Enter q value: "))
    n = p * q
    print(f"\np = {p}, q = {q}, n = {n}")
    
    # Compute Euler's totient function, phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)
    
    # Find possible values of e where gcd(e, phi(n)) = 1
    possible_e_values = [e for e in range(2, phi) if gcd(e, phi) == 1]
    print(f"\nPossible values of e (that are coprime with phi(n)):\n{possible_e_values}")
    e = int(input("\nSelect an e value from the list: "))
    
    # Compute the modular inverse of e, d = e^(-1) mod phi(n)
    d = mod_inverse(e, phi)
    
    print(f"Public Key (e={e}, n={n})")
    print(f"Private Key (d={d}, n={n})")
    
    # Return the public and private keys
    return (e, n), (d, n)

def encrypt(M, public_key):
    e, n = public_key
    C = pow(M, e, n)
    return C

def decrypt(C, private_key):
    d, n = private_key
    decrypted_message = pow(C, d, n)
    return decrypted_message


public_key, private_key = generate_keys()
M = int(input("\nEnter numeric value to encrypt: "))
C = encrypt(M, public_key)
print(f"Encrypted message: {C}")
K = int(input("\nEnter numeric value to decrypt: "))
decrypted_message = decrypt(K, private_key)
print(f"Decrypted message: {decrypted_message}")
