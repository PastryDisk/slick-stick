from cryptography.fernet import Fernet
import key_management

def decrypt_file(file):
    with open(key_management.get_key_file(), 'rb') as f:
        key = f.read()

    fe = Fernet(key)

    with open(file, 'rb') as f:
        data = f.read()

    encrypted = fe.decrypt(data)

    file = file[:-4]

    with open(file, 'wb') as f:
        f.write(encrypted)

def passwd_decrypt(password):
    if key_management.check_passwd(password):
        with open(key_management.get_passwd_key_file(), 'rb') as f:
            key = f.read()

        fe = Fernet(key)

        with open(key_file, 'rb') as f:
            data = f.read()

        encrypted = fe.decrypt(data)

        key_file = key_file[:-4]

        with open(key_file, 'wb') as f:
            f.write(encrypted)
    else: 
        print("Incorrect Password")