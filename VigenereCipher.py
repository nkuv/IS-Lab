def vigenere(text, key, mode):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if mode == "decrypt":
                shift = -shift
                
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index = (key_index + 1) % len(key)
        else:
            result += char

    return result

text = input("Enter plaintext: ")
key = input("Enter keyword: ")
encrypted = vigenere(text, key,"encrypt")
print(f'Encrypted text: {encrypted}')

cipher = input("\nEnter ciphertext: ")
decrypted = vigenere(cipher, key,"decrypt")
print(f'Decrypted text: {decrypted}')

