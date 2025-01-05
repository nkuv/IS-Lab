import numpy as np

def mod_inverse(a, m): # Find modular inverse using extended Euclidean algorithm
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % modulus, modulus)
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_mod_inv

def encrypt(plaintext, key):
    key_matrix = np.array(key)
    plaintext_numbers = [ord(char) - ord('A') for char in plaintext.upper() if char.isalpha()]

    if len(plaintext_numbers) % 2 != 0:
        plaintext_numbers.append(ord('X') - ord('A'))

    ciphertext = ''
    for i in range(0, len(plaintext_numbers), 2):
        vector = np.array(plaintext_numbers[i:i+2])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        ciphertext += ''.join(chr(num + ord('A')) for num in encrypted_vector)
    
    return ciphertext

def decrypt(ciphertext, key):
    key_matrix = np.array(key)
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext.upper() if char.isalpha()]

    plaintext = ''
    for i in range(0, len(ciphertext_numbers), 2):
        vector = np.array(ciphertext_numbers[i:i+2])
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26
        plaintext += ''.join(chr(int(num) + ord('A')) for num in decrypted_vector)

    return plaintext

key = [[3, 3], [2, 5]]
print(f'key = {key}')
plaintext = input("\nEnter a plaintext: ")
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

ciphertext = input("\nEnter a ciphertext: ")
decrypted_text = decrypt(ciphertext, key)
print(f"Decrypted: {decrypted_text}")