# Image Encrypter and Decrypter

This project contains two Python scripts, `encryption.py` and `decryption.py`, which allow you to encrypt and decrypt image files using a simple XOR-based encryption method.

## Features

- **Encryption**: Encrypts an image file using a user-provided key.
- **Decryption**: Decrypts an encrypted image file using the same key used for encryption.

## Files

### 1. `encryption.py`
This script encrypts an image file by performing an XOR operation on its byte data with a user-provided key.

#### How it works:
1. Prompts the user to input the path of the image file.
2. Prompts the user to input an encryption key (integer).
3. Reads the image file in binary mode.
4. Converts the image data into a byte array.
5. Performs an XOR operation on each byte using the provided key.
6. Writes the encrypted data back to the image file.

#### Usage:
```bash
python encryption.py
```

### 2. `decryption.py`
This script decrypts an encrypted image file by performing an XOR operation on its byte data with the same key used for encryption.

#### How it works:
1. Prompts the user to input the path of the encrypted image file.
2. Prompts the user to input the decryption key (must be the same as the encryption key).
3. Reads the encrypted image file in binary mode.
4. Converts the image data into a byte array.
5. Performs an XOR operation on each byte using the provided key.
6. Writes the decrypted data back to the image file.

#### Usage:
```bash
python decryption.py
```

## Important Notes

- **Key Consistency**: The encryption and decryption keys must be the same for the process to work correctly.
- **File Overwriting**: The scripts overwrite the original image file with the encrypted or decrypted data. Make sure to back up your files before running the scripts.
- **Error Handling**: Both scripts include basic error handling to catch and display exceptions.

## Example

1. Encrypt an image:
   ```bash
   python encryption.py
   ```
   - Enter the path of the image file (e.g., `C:\path\to\image.jpg`).
   - Enter an encryption key (e.g., `123`).

2. Decrypt the image:
   ```bash
   python decryption.py
   ```
   - Enter the path of the encrypted image file.
   - Enter the same key used for encryption (e.g., `123`).

## Requirements

- Python 3.x
- No additional libraries are required.

## Disclaimer

This project uses a simple XOR-based encryption method, which is not secure for sensitive data. It is intended for educational purposes or basic use cases only. For secure encryption, consider using established cryptographic libraries like `cryptography` or `PyCrypto`.

## License

This project is open-source and available under the MIT License.
# Image Encrypter and Decrypter

This project contains two Python scripts, `encryption.py` and `decryption.py`, which allow you to encrypt and decrypt image files using the `cryptography` library.

## Features

- **Encryption**: Encrypts an image file using a secure key generated by the `cryptography` library.
- **Decryption**: Decrypts an encrypted image file using the saved key.

## Files

### 1. `encryption.py`
This script encrypts an image file using the `cryptography` library.

#### How it works:
1. Generates a secure encryption key using `Fernet.generate_key()`.
2. Saves the key to a file (`encryption_key.key`) for later use.
3. Prompts the user to input the path of the image file.
4. Reads the image file in binary mode.
5. Encrypts the image data using the generated key.
6. Writes the encrypted data back to the image file.

#### Usage:
```bash
python encryption.py
```

### 2. `decryption.py`
This script decrypts an encrypted image file using the saved key.

#### How it works:
1. Loads the encryption key from the `encryption_key.key` file.
2. Prompts the user to input the path of the encrypted image file.
3. Reads the encrypted image file in binary mode.
4. Decrypts the image data using the loaded key.
5. Writes the decrypted data back to the image file.

#### Usage:
```bash
python decryption.py
```

## Important Notes

- **Key Management**: The encryption key is saved to a file (`encryption_key.key`). Do not lose this file, as it is required for decryption.
- **File Overwriting**: The scripts overwrite the original image file with the encrypted or decrypted data. Make sure to back up your files before running the scripts.
- **Error Handling**: Both scripts include basic error handling to catch and display exceptions.

## Example

1. Encrypt an image:
   ```bash
   python encryption.py
   ```
   - Enter the path of the image file (e.g., `C:\path\to\image.jpg`).

2. Decrypt the image:
   ```bash
   python decryption.py
   ```
   - Enter the path of the encrypted image file.

## Requirements

- Python 3.x
- `cryptography` library (install using `pip install cryptography`)

## Disclaimer

This project uses the `cryptography` library for secure encryption. Ensure the encryption key is stored securely, as losing it will make decryption impossible.

## License

This project is open-source and available under the MIT License.
