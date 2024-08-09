import random
from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime, inverse

def generate_prime(bits):
    """Generate a prime number with the specified number of bits."""
    return getPrime(bits)

print("--------------------------")
print("key generation")

# Generate a prime number p
p = generate_prime(512)  # Adjust the number of bits as needed

# Choose a generator g (this is an arbitrary choice; it should be a primitive root modulo p)
g = 6

# Private key x (chosen randomly)
x = random.randint(1, p-2)

# Calculate y = g^x mod p
y = pow(g, x, p)

print("public key: (p=", p, ", g=", g, ", y=", y, ")")
print("private key: ", x)

print("--------------------------")
print("encryption")

# Encryption
m = 100
k = random.randint(1, p-1)

c1 = pow(g, k, p)
c2 = m * pow(y, k, p) % p

print("ciphertext: (c1=", c1, ", c2=", c2, ")")

# Bob sends c1, c2 pair to Alice

print("----------------------------")
print("decryption")

# Decryption
# Calculate the modular inverse of c1
c1_inv = inverse(c1, p)
restored = c2 * pow(c1_inv, x, p) % p
print("restored message: ", restored)
