def caesar_encrypt(text,shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) + shift - base) % 26
            encrypted += chr(base + shifted)
        else:
            encrypted += char
    return encrypted

plaintext = input("Enter a plaintext: ")
shift = 3
ciphertext = caesar_encrypt(plaintext,shift)
print("Encrypted Text:", ciphertext)
