from cryptography.fernet import Fernet
import bcrypt, app

def generate_file_key(key_file):
    master_key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(master_key)

def create_passwd(passw, passwd_file):
    passwd = passw.encode("utf-8")
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    with open(passwd_file, 'wb') as f:
        f.write(hashed)
    return hashed

def check_passwd(passw):
    hashed = app.passw_file
    passwd = passw.encode("utf-8")
    if bcrypt.checkpw(passwd, hashed):
        return True
    else:
        return False