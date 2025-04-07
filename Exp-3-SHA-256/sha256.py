from hashlib import sha256

msg1 = input("First message: ")
msg2 = input("Second message: ")

h1 = sha256(msg1.encode()).hexdigest()
h2 = sha256(msg2.encode()).hexdigest()

print("\nH1 =", h1)
print("H2 =", h2)

int1 = int(h1, 16)
int2 = int(h2, 16)

xor = int1 ^ int2
bits_changed = bin(xor).count('1')

print("\nBit difference:", bits_changed)
