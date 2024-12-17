def ceaser_cipher(text,key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted =  (ord(char) + key - base) % 26
            encrypted += chr(base + shifted)
        else:
            encrypted += char
    return encrypted

plaintext = input("Enter a plaintext: ")
key = 3
ciphertext = ceaser_cipher(plaintext,key)
print("Encrpted text:",ciphertext)

