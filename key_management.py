from cryptography.fernet import Fernet
import bcrypt

key_file = r'C:\Users\jakob\OneDrive\Documents\Grizzhacks 4\Key Files\masterkey.txt'
passwd_file = r'C:\Users\jakob\OneDrive\Documents\Grizzhacks 4\Key Files\passwd.txt'
passwd_key_file = r'C:\Users\jakob\OneDrive\Documents\Grizzhacks 4\Key Files\passwd_key.txt'

def get_key_file():
    return key_file

def get_passwd_file():
    return passwd_file

def get_passwd_key_file():
    return passwd_key_file

def generate_file_key():
    master_key = Fernet.generate_key()
    master_key1 = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(master_key)
    with open(passwd_key_file, 'wb') as f:
        f.write(master_key1)

def create_passwd(password):
    passwd = password.encode("utf-8")
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    with open(passwd_file, 'wb') as f:
        f.write(hashed)
    return hashed

def check_passwd(password):
    with open(passwd_file, 'rb') as f:
        hashed = f.read()
    
    passwd = password.encode("utf-8")

    if bcrypt.checkpw(passwd, hashed):
        return True
    else:
        return False