import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# This script demonstrates a basic application of a Diffie-Hellman key exchange-like mechanism
# followed by AES encryption in CBC mode.

# Generate public parameters
mod = random.getrandbits(512)  # A large random number; in practice, this should be a large prime number.
g = 6  # Base generator, typically a small integer.

print("public information:")
print("mod:", mod)
print("base generator:", g)
print("--------------------")

# Alice generates her private and public key pair
alicePrivate = random.getrandbits(512)
alicePublic = pow(g, alicePrivate, mod)
print("alice public:", alicePublic)

# Bob generates his private and public key pair
bobPrivate = random.getrandbits(512)
bobPublic = pow(g, bobPrivate, mod)
print("bob public:", bobPublic)
print("--------------------")

# Both parties compute the shared secret
aliceShared = pow(bobPublic, alicePrivate, mod)
bobShared = pow(alicePublic, bobPrivate, mod)
assert aliceShared == bobShared  # Verify both shared secrets are equal

print("-alice shared:", aliceShared)
print("\n-bob shared:", bobShared)
print("--------------------")

# Message to be encrypted
message = "hi alice, howdy?"

# Generate a 32-byte key from the shared secret
key = str(aliceShared).encode('utf-8')[:32]  # Extract the first 32 bytes of the shared secret
key = key.ljust(32, b'\0')  # Pad the key to ensure it is exactly 32 bytes

# Initialize AES cipher in CBC mode with a random IV
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the message to ensure it is a multiple of the block size (16 bytes for AES)
padded_message = pad(message.encode('utf-8'), AES.block_size)

# Encrypt the message
ciphertext = cipher.encrypt(padded_message)
print("ciphertext:", ciphertext)

# Decrypt the message to verify correctness
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
decrypted_padded_message = cipher_dec.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded_message, AES.block_size)
print("decrypted message:", decrypted_message.decode('utf-8'))
print("--------------------")

# Bob uses the same key and IV to decrypt the ciphertext
bob_key = str(bobShared).encode('utf-8')[:32]  # Ensure key handling is consistent with encryption
bob_key = bob_key.ljust(32, b'\0')
cipher_bob = AES.new(bob_key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
plaintext_padded = cipher_bob.decrypt(ciphertext)
plaintext = unpad(plaintext_padded, AES.block_size)
print("plaintext:", plaintext.decode('utf-8'))
