from cryptography.fernet import Fernet
import bcrypt, app

def get_key_file():
    return app.key_file

def get_passwd_file():
    return app.passw_file

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
    hashed = get_passwd_file()
    
    passwd = passw.encode("utf-8")

    if bcrypt.checkpw(passwd, hashed):
        return True
    else:
        return False