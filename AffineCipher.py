from math import gcd

def mod_inverse(a,m):
    for x in range(1,m):
        if(a*x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} and 26")

def affine_encrypt(text,a,b):
    if gcd(a,26)!=1:
        print(f"Key a={a} is invalid. gcd(a,26) must be 1")
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
  
def affine_decrypt(text,a,b):
    if gcd(a,26)!=1:
        print(f"Key a={a} is invalid. gcd(a,26) must be 1")
        exit()     
    a_inv = mod_inverse(a,26)
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            x = (a_inv * ((ord(char) - base) - b)) % 26
            decrypted += chr(base + x)
        else:
            decrypted += char
    return decrypted
    
plaintext = input("Enter a plaintext: ")
a = int(input("Enter a-key: "))
b = int(input("Enter b-key: "))
ciphertext = affine_encrypt(plaintext,a,b)
print("Encrypted text:",ciphertext)

ciphertext = input("\nEnter a ciphertext: ")
a = int(input("Enter a-key: "))
b = int(input("Enter b-key: "))
plaintext = affine_decrypt(ciphertext,a,b)
print("Decrypted text:",plaintext)

        
    

    
