import hashlib

s1 = input("Enter first string: ")
h1 = hashlib.sha256(s1.encode()).hexdigest()
print(f"H1 (hex): {h1}")

s2 = input("\nEnter second string: ")
h2 = hashlib.sha256(s2.encode()).hexdigest()
print(f"H2 (hex): {h2}")

h1_bytes = bytes.fromhex(h1)
h2_bytes = bytes.fromhex(h2)

h1_int = int.from_bytes(h1_bytes,byteorder='big')
h2_int = int.from_bytes(h2_bytes,byteorder='big')

xor_result = h1_int ^ h2_int
bit_difference = bin(xor_result).count('1')

print(f"\nNumber of differing bits: {bit_difference}")