from cryptography.fernet import Fernet

try:
    # Load the encryption key
    with open('encryption_key.key', 'rb') as key_file:
        key = key_file.read()
    cipher = Fernet(key)

    # Take the path of the encrypted image as input
    path = input(r'Enter path of Encrypted Image: ')

    # Open the encrypted image file in binary read mode
    with open(path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the image data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(path, 'wb') as file:
        file.write(decrypted_data)

    print('Decryption Done.')

except Exception as e:
    print('Error caught:', e)