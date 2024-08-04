import random
import time

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def modInverse(e, totient):
    """Find the modular inverse of e modulo totient using the Extended Euclidean Algorithm."""
    x1, x2, x3 = 1, 0, totient
    y1, y2, y3 = 0, 1, e

    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    
    if x3 == 1:
        return x2 % totient

# Start time measurement
start_time = time.time()

# Define large prime numbers
p = 32452843
q = 104729

# Calculate modulus and totient
n = p * q
totient = (p - 1) * (q - 1)

print(f"Modulus (n): {n}")
print(f"Totient function (φ): {totient}")
print("-------------------------------")

# Generate public exponent e such that 1 < e < totient and gcd(e, totient) = 1
e = random.randint(1, totient)
while gcd(totient, e) != 1:
    e = random.randint(1, totient)

print(f"Public key (e): {e}")

# Calculate private key d
d = modInverse(e, totient)
print(f"Private key (d): {d}")

# Key generation time
keygen_time = time.time() - start_time
print(f"Key generation complete in {keygen_time:.4f} seconds")
print("------------------------------------------")

# Encrypt a message m
m = 15
ciphertext = pow(m, e, n)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
restored = pow(ciphertext, d, n)
print(f"Restored message: {restored}")

# Total time for encryption and decryption
total_time = time.time() - start_time
print(f"Decryption complete in {total_time:.4f} seconds")
