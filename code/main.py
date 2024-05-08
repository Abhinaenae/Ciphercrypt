import caesar
import vigenere


def continuation():
    while True:
        response = input("Would you like to continue? (yes/y or no/n): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            exit()
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


while True:
    print("\nOption 1: Convert String to Caesar Cipher", "\nOption 2: Convert String to Vigenere Cipher", "\nOption 3: Exit Program")
    option = input("Which option do you want to select [Enter 1, 2, or 3]? ")

    if option == '1':
        msg = input("Enter message: ")
        shift = input("Enter shift value: ")
        if shift.isdigit():
            shift = int(shift)
            encrypted = caesar.caesar(msg, shift)
            print(f'\nEncrypted text: {encrypted}\n')
            if not continuation():
                exit()
        else:
            print("Shift value must be an integer.\n")

    elif option == '2':
        msg = input("Enter message: ")
        custom_key = input("Enter key: ")
        eord = input("Encrypt or Decrypt? ")

        if eord.lower() in ["encrypt", "e", "1"]:
            encryption = vigenere.encrypt(msg, custom_key)
            print(f'\nEncrypted text: {encryption}\n')
            if not continuation():
                exit()
        elif eord.lower() in ["decrypt", "d", "2"]:
            decryption = vigenere.decrypt(msg, custom_key)
            print(f'\nDecrypted text: {decryption}\n')
            if not continuation():
                exit()
        else:
            print("Invalid input! Please enter 'encrypt' or 'decrypt'.\n")

    elif option == '3':
        exit()

    else:
        print("Invalid option! Please select again.\n")
