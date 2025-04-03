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


key = int(input("Enter shift parameter: "))

plaintext = input("\nEnter plaintext: ")
ciphertext = ceaser_encrypt(plaintext,key)
print("Encrypted Text:",ciphertext)

ciphertext = input("\nEnter ciphertext: ")
plaintext = ceaser_encrypt(ciphertext,-key)
print("Decrypted Text:",plaintext)




