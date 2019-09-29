from cryptography.fernet import Fernet
import key_management, os, app

def decrypt_file(file):
    key = app.key_file

    fe = Fernet(key)

    with open(file, 'rb') as f:
        data = f.read()

    encrypted = fe.decrypt(data)

    file = file[:-4]

    with open(file, 'wb') as f:
        f.write(encrypted)


