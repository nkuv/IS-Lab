def affine_encrypt(text, a, b):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (a * (ord(char) - base) + b) % 26
            encrypted += chr(base + shifted)
        else:
            encrypted += char
    return encrypted


def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26) 
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (a_inv * ((ord(char) - base) - b)) % 26
            decrypted += chr(base + shifted)
        else:
            decrypted += char
    return decrypted


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

plaintext = input("Enter a plaintext: ")
a, b = 5, 8
ciphertext = affine_encrypt(plaintext, a, b)
print("Encrypted Text:", ciphertext)

ciphertext = input("\nEnter a ciphertext: ")
plaintext = affine_decrypt(ciphertext, a, b)
print("Decrypted Text:", plaintext)
