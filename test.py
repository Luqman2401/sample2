from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from hashlib import md5
import os

def encrypt_image(image_path, key):
    # Read the image file
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Create a Triple DES key from the provided key
    key_hash = md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)

    # Create a Triple DES cipher object
    cipher = DES3.new(tdes_key, DES3.MODE_ECB)

    # Pad the image data to a multiple of the block size
    padded_data = pad(image_data, DES3.block_size)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Save the encrypted data to a new file
    encrypted_image_path = image_path + '.encrypted'
    with open(encrypted_image_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"Encrypted image saved to {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    # Read the encrypted image file
    with open(encrypted_image_path, 'rb') as file:
        encrypted_data = file.read()

    # Create a Triple DES key from the provided key
    key_hash = md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)

    # Create a Triple DES cipher object
    cipher = DES3.new(tdes_key, DES3.MODE_ECB)

    # Decrypt the encrypted data
    decrypted_padded_data = cipher.decrypt(encrypted_data)

    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_padded_data, DES3.block_size)

    # Save the decrypted data to a new file
    decrypted_image_path = encrypted_image_path[:-10]  # Remove the '.encrypted' extension
    with open(decrypted_image_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"Decrypted image saved to {decrypted_image_path}")

# Example usage
image_path = '/home/kali/desktop/sample.jpeg'
key = 'y_secret_key'

encrypt_image(image_path, key)
decrypt_image(image_path + '.encrypted', key)
