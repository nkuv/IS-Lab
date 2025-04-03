from math import gcd

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        print(f"Invalid key: gcd(a, 26) must be 1")
        exit()

    encrypted = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted = (a * (ord(char) - base) + b) % 26
            encrypted += chr(base + shifted)
        else:
            encrypted += char
    return encrypted

def affine_decrypt(text, a, b):
    if gcd(a, 26) != 1:
        print(f"Invalid key: gcd(a, 26) must be 1")
        exit()

    a_inv = pow(a, -1, 26)
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted = (a_inv * ((ord(char) - base) - b)) % 26
            decrypted += chr(base + shifted)
        else:
            decrypted += char
    return decrypted


a = int(input("Enter a-key: "))
b = int(input("Enter b-key: "))

plaintext = input("\nEnter plaintext: ")
ciphertext = affine_encrypt(plaintext,a,b)
print("Encrypted text:",ciphertext)

ciphertext = input("\nEnter ciphertext: ")
plaintext = affine_decrypt(ciphertext,a,b)
print("Decrypted text:",plaintext)