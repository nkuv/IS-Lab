def ceaser_encrypt(text,key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) + key - base) % 26
            encrypted += chr(base + shifted)
        else:
            encrypted += char
    return encrypted

def ceaser_bruteforce(ciphertext):
    for key in range(26):
        print(f"Key {key} : {ceaser_encrypt(ciphertext,-key)}")

plaintext = input("Enter a plaintext: ")
key = 3
ciphertext = ceaser_encrypt(plaintext,key)
print("Encrypted Text:",ciphertext)

ciphertext = input("\nEnter a ciphertext: ")
plaintext = ceaser_encrypt(ciphertext,-key)
print("Decrypted Text:",plaintext)

print("\nBrute force attack result: ")
ceaser_bruteforce(ciphertext)



