from cryptography.fernet import Fernet

try:
    # Generate or load a key
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Save the key to a file for later decryption
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)

    # Take the path of the image as input
    path = input(r'Enter path of Image: ')

    # Open the image file in binary read mode
    with open(path, 'rb') as file:
        image_data = file.read()

    # Encrypt the image data
    encrypted_data = cipher.encrypt(image_data)

    # Write the encrypted data back to the file
    with open(path, 'wb') as file:
        file.write(encrypted_data)

    print('Encryption Done. Key saved to "encryption_key.key".')

except Exception as e:
    print('Error caught:', e)