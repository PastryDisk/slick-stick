import key_management, encrypt
import UIfunctions
import sys

def run():
    text = input("Please enter a password: ")
    print("Your password is: " + text)
    print("Your password hash is: " + str(key_management.create_passwd(text)))
    text2 = input("Please enter your password again: ")
    print(key_management.check_passwd(text2))
    key_management.generate_file_key()

    file_encry = input("Would you like to encrypt a file? (Y/n) ")
    if (file_encry == "Y"):
        file_name = input("What file would you like to encrypt?")
        encrypt.encrypt_file("C:/Users/jakob/OneDrive/Documents/Grizzhacks 4/Files/" + file_name)

UIfunctions.browse_vault()