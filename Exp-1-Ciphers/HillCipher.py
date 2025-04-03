import numpy as np

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = pow(det, -1, modulus) 
    matrix_mod_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus
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
print(f'Key: {key}')

plaintext = input("\nEnter plaintext: ")
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

ciphertext = input("\nEnter ciphertext: ")
decrypted_text = decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
