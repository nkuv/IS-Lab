def vigenere_encrypt(text, key):
    key = key.upper()
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index = (key_index + 1) % len(key)
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    key = key.upper()
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift + 26) % 26 + base)
            key_index = (key_index + 1) % len(key)
        else:
            result += char

    return result


text = input("Enter plaintext: ").upper()
key = input("Enter keyword: ").upper()
encrypted = vigenere_encrypt(text, key)
print(f'Encrypted text: {encrypted}')

cipher = input("\nEnter ciphertext: ").upper()
decrypted = vigenere_decrypt(encrypted, key)
print(f'Decrypted text: {decrypted}')

