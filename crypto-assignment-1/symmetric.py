# Anthony Habib - 100662176
# October 4th 2019

import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

# User enters their message
print("You are encrypting with AES")
plain_text = input("Enter your plaintext:")
plaintext_to_bytes = bytes(plain_text, 'utf-8')

# Padding adds random text to fit the block size
padder = padding.PKCS7(128).padder()
padder_data = padder.update(plaintext_to_bytes)
padder_data += padder.finalize()

# Key and IV will generate 32 and 16 random characters
mykey = os.urandom(32)
initial_value = os.urandom(16)

# Generates the AES encryption method
cipher = Cipher(algorithms.AES(mykey), modes.CBC(initial_value), backend=backend)

# Used to encrypt our plaintext
encrypt = cipher.encryptor()
encrypt_text = encrypt.update(padder_data) + encrypt.finalize()

# Used to decrypt our encrypted text
decrypt = cipher.decryptor()
decrypt_text = decrypt.update(encrypt_text) + decrypt.finalize()

# Takes out the random text from out cipher
unpadder = padding.PKCS7(128).unpadder()
unpadder_data = unpadder.update(decrypt_text)
original_message = unpadder_data + unpadder.finalize()

# Prints our encrypted and decrypted message
print("Your encrypted text will look like:", encrypt_text)
print("Your original message was:", original_message)

