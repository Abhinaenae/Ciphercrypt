# Ciphercrypt, a CLI Encryption/Decryption Tool

This command-line tool, written in Python3, provides functionalities to encrypt or decrypt text using Caesar Cipher or Vigenere Cipher. It offers a simple interface for users to perform encryption and decryption operations on their text data.

## Features

- Supports encryption and decryption using both Caesar Cipher and Vigenere Cipher
- Simple command-line interface for ease of use.
- Additional cipher formats may be added in future updates.

## Usage

1. Clone or download the repository.
2. Navigate to the directory containing the script files.
3. Run the script using Python (`python main.py`).
4. Follow the prompts to select the cipher type (Caesar or Vigenere), enter the text, and provide any required parameters (such as shift value or encryption key).
5. View the encrypted or decrypted text as the output.

Examples:
```
python3 main.py
Option 1: Convert String to Caesar Cipher 
Option 2: Convert String to Vigenere Cipher
Option 3: Exit Program
Which option do you want to select [Enter 1,2, or 3]? 1
Enter message: hello
Enter shift value: 3

Encrypted text: khoor
```

```
Would you like to continue?y
Option 1: Convert String to Caesar Cipher
Option 2: Convert String to Vigenere Cipher
Option 3: Exit Program
Which option do you want to select [Enter 1,2, or 3]? 2
Enter message: hello
Enter key: nope
Encrypt or Decrypt?e

Encrypted text: usapb
```
```
Which option do you want to select [Enter 1,2, or 3]? 2
Enter message: usapb
Enter key: nope
Encrypt or Decrypt?d

Decrypted text: hello
```
## Contribution

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.



