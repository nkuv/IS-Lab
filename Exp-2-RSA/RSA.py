# public key(e) must satisfy the condition 1 < e < phi(n) and gcd(e, phi(n)) = 1

from sympy import mod_inverse, gcd

def generate_keys():
    p = int(input("Enter p value: "))
    q = int(input("Enter q value: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    
    possible_e_values = [e for e in range(2, phi) if gcd(e, phi) == 1]  
    print(f"\nPossible values of e:\n{possible_e_values}")

    e = int(input("\nSelect an e value: "))
    d = mod_inverse(e, phi)

    print(f"Public Key (e={e}, n={n})")
    print(f"Private Key (d={d}, n={n})")
    return (e, n), (d, n)

def encrypt(M, public_key):
    e, n = public_key
    C = pow(M, e, n)
    return C

def decrypt(C, private_key):
    d, n = private_key
    M = pow(C, d, n)
    return M


public_key, private_key = generate_keys()

M = int(input("\nEnter numeric value to encrypt: "))
C = encrypt(M, public_key)
print(f"Encrypted message: {C}")

C = int(input("\nEnter numeric value to decrypt: "))
M = decrypt(C, private_key)
print(f"Decrypted message: {M}")
