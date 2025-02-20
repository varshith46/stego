# SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY

This project provides a simple implementation of **image-based steganography**, where secret messages are hidden within an image and later retrieved using a decryption script. The encryption and decryption processes involve modifying the pixel values of an image to store message bytes.

## Features

- Hide a secret message inside an image using pixel manipulation.
- Secure the message with a password.
- Extract the hidden message only with the correct password.
- Simple and lightweight implementation using Python and OpenCV.

## Requirements

Make sure you have the following dependencies installed before running the scripts:

```sh
pip install opencv-python
```

## Usage

### 1. Encrypting a Message

To hide a secret message in an image:

```sh
python encrypt.py
```

#### Steps:

1. The script will ask for the image file (`mypic.jpg`).
2. Enter the secret message you want to hide.
3. Provide a password for security.
4. The encrypted image is saved as `encryptedImage.png`.
5. The password is stored in `key.txt`.

### 2. Decrypting a Message

To retrieve the hidden message from the encrypted image:

```sh
python decrypt.py
```

#### Steps:

1. The script reads `encryptedImage.png`.
2. You must enter the correct password.
3. If the password matches, the hidden message is displayed.
4. If the password is incorrect, access is denied.

## File Descriptions

- **encrypt.py** - Script to embed a secret message into an image.
- **decrypt.py** - Script to extract the secret message from the image.
- **encryptedImage.png** - Image containing the hidden message.
- **key.txt** - Stores the password required for decryption.
- **mypic.jpg** - Original image used for encryption.

## Example

### Encrypting:

```sh
Enter secret message: varu@46
Enter a passcode: 562004
Encryption done. Saved as 'encryptedImage.png'.
```

### Decrypting:

```sh
Enter password: 562004
Secret message: varu@46
```

## Notes

- The encryption process replaces pixel values with message bytes.
- The message length should not exceed the image size.
- A NULL (`\0`) byte is used as an end marker to detect the message termination.
