from cryptography.fernet import Fernet
import key_management


def encrypt_file(file):
    key = key_management.get_key_file()

    fe = Fernet(key)

    with open(file, 'rb') as f:
        data= f.read()

    encrypted = fe.encrypt(data)

    with open(file + ".enc", 'wb') as f:
        f.write(encrypted)
    
    return encrypted

