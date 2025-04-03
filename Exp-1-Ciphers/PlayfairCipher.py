import numpy as np

def find_char_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i, j] == char:
                return i, j
    return -1,-1

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []
    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
            
    return np.array(key_matrix).reshape(5, 5)

def process_pairs(text):
    text = text.upper().replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            pairs.append(text[i] + 'X')
            i += 1
        else:
            pairs.append(text[i:i + 2])
            i += 2
    if len(pairs[-1]) == 1:
        pairs[-1] += 'X'
        
    return pairs

def playfair_cipher(matrix, text, mode="encrypt"):
    shift = 1 if mode == "encrypt" else -1
    pairs = process_pairs(text)
    result = ""

    for a, b in pairs:
        row1, col1 = find_char_position(matrix, a)
        row2, col2 = find_char_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 + shift) % 5] + matrix[row2][(col2 + shift) % 5]
        elif col1 == col2:
            result += matrix[(row1 + shift) % 5][col1] + matrix[(row2 + shift) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]

    return result


key = input("Enter key: ")
matrix = generate_key_matrix(key)

plaintext = input("\nEnter plaintext: ").replace(" ","")
ciphertext = playfair_cipher(matrix,plaintext,mode="encrypt")
print(f"Ciphertext: {ciphertext}")

ciphertext = input("\nEnter ciphertext: ")
decrypted_text = playfair_cipher(matrix,ciphertext,mode="decrypt")
print(f"Decrypted text: {decrypted_text}")