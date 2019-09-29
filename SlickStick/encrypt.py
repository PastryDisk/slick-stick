from cryptography.fernet import Fernet
import key_management, app


def encrypt_file(file):
    x = file.split("/")

    l = len(x)

    key = app.key_file

    fe = Fernet(key)

    with open(file, 'rb') as f:
        data= f.read()

    encrypted = fe.encrypt(data)

    name = app.vault_path + "/" + x[l-1]

    with open(name + ".enc", 'wb') as f:
        f.write(encrypted)
    

