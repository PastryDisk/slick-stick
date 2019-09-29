import PySimpleGUI as sg
import os.path, encrypt, decrypt, setup


def initialize_filepaths():
    dirname = os.path.dirname(__file__)
    USB = os.path.join(dirname, 'USBfilepath.txt')
    vault = os.path.join(dirname, 'vaultfilepath.txt')

    with open(USB, 'r') as f:
        USB_path = f.read()

    with open(vault, 'r') as f:
        vault_path = f.read()

    key_path = USB_path + "/key.txt"
    passw_path = USB_path + "/password.txt"

    if (os.path.isfile(key_path)):
        with open(key_path, 'rb') as f:
            key_file = f.read()

        with open(passw_path, 'rb') as f:
            passw_file = f.read()

        return USB_path, vault_path, key_file, passw_file
    else:
        filename = os.path.join(dirname, 'logo.png')
        layout = [[sg.Image(filename)],
                [sg.Text('Please insert your Slick Stick USB')],       
                [sg.Ok()]]     

        window = sg.Window('Initial Setup', layout)  

        event, values = window.Read() 
        window.Close() 
        app()

if(setup.setup_file == "1"):
    USB_path, vault_path, key_file, passw_file = initialize_filepaths()

def login():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'logo.png')

    layout = [[sg.Image(filename)],
            [sg.Text('Enter your password')],    
            [sg.Text('Password', size=(10, 1)), sg.Input(password_char="*")],          
            [sg.Submit(), sg.Cancel()]]        

    window = sg.Window('Slick Stick Login', layout)  

    event, values = window.Read()

    window.Close()

    import key_management
    if(key_management.check_passwd(values[1])) :
        app()
    else:
        login()

 

def app():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'logo.png')

    layout = [[sg.Image(filename)],    
             [sg.Button(button_text="Encrypt Files"), sg.Button(button_text="Decrypt Files")]]      

    window = sg.Window('Slick Stick', layout)  

    event, values = window.Read()  

    window.Close()

    if(event == "Encrypt Files"):
        encrypt_app()
        app()
    elif(event == "Decrypt Files"):
        decrypt_app()
        app()

def encrypt_app():    
    layout = [[sg.Text('Select the files to encrypt')],
            [sg.Input(), sg.FilesBrowse()], 
            [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Encrypt Files', layout)
    event, values = window.Read()  
    window.Close()

    if(event == "Cancel"):
        app()

    x = values[0].split(";")
    a = len(x)
    for i in range(a) :
        encrypt.encrypt_file(x[i])
 

def decrypt_app():
    layout = [[sg.Text('Select the files to decrypt')],
            [sg.Input(), sg.FilesBrowse(file_types=(("Encrypted Files", "*.enc"), ))], 
            [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Decrypt Files', layout)
    event, values = window.Read()  
    window.Close()

    if(event == "Cancel"):
        app()

    x = values[0].split(";")
    a = len(x)
    for i in range(a) :
        decrypt.decrypt_file(x[i])
        os.remove(x[i])
    