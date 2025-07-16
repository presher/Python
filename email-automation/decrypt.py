from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to decrypt the API key
def decrypt_api_key():
    # Load the encryption key
    key = os.getenv('ENCRYPTION_KEY').encode()

    # Initialize the cipher with the loaded key
    cipher = Fernet(key)

    # Load the encrypted API key
    
    # with open('encrypted_api_key.txt', 'rb') as encrypted_file:
     #   encrypted_api_key = encrypted_file.read()

    # Decrypt the API key
    decrypted_api_key = cipher.decrypt(os.getenv('OPEN_API_KEY_ENC')).decode()
    
    return decrypted_api_key

# Usage in your program
#decrypt_api_key()
