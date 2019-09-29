from cryptography.fernet import Fernet
import key_management, os

def encrypt_file(file):
    with open(key_management.get_key_file(), 'rb') as f:
        key = f.read()

    fe = Fernet(key)

    with open(file, 'rb') as f:
        data= f.read()

    encrypted = fe.encrypt(data)

    with open(file + ".enc", 'wb') as f:
        f.write(encrypted)

    os.remove(file)
    
    return encrypted

    

def passwd_encrypt():
    with open(key_management.get_passwd_key_file(), 'rb') as f:
        key = f.read()

    fe = Fernet(key)

    with open(key_management.key_file, 'rb') as f:
        data= f.read()

    encrypted = fe.encrypt(data)

    with open(key_management.key_file + ".enc", 'wb') as f:
        f.write(encrypted)
