from cryptography.fernet import Fernet
import os

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Store this key safely, as you will need it to decrypt the API key
with open('encryption_key.key', 'wb') as key_file:
    key_file.write(key)

# API key to be encrypted
api_key = API_KEY
print(api_key)
# Encrypt the API key
encrypted_api_key = cipher.encrypt(api_key.encode())

# Store the encrypted API key in a file
with open('encrypted_api_key.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_api_key)

print("API Key encrypted successfully.")
