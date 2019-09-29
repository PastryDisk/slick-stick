import PySimpleGUI as sg
import os.path, encrypt

def initialize_filepaths():
    with open('USBfilepath.txt', 'r') as file:
        USB_path = file.read()

    with open('vaultfilepath.txt', 'r') as file:
        vault_path = file.read()

    key_path = USB_path + "/key.txt"
    passw_path = USB_path + "/password.txt"

    with open(key_path, 'r') as file:
        key_file = file.read()

    with open(passw_path, 'r') as file:
        passw_file = file.read()

def login():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../Files/logo.png')

    layout = [[sg.Image(filename)],
            [sg.Text('Enter your password')],    
            [sg.Text('Password', size=(10, 1)), sg.Input()],          
            [sg.Submit(), sg.Cancel()]]        

    window = sg.Window('Slick Stick Login', layout)  

    event, values = window.Read()  

    window.Close()

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
    elif(event == "Decrypt Files"):
        decrypt_app()

def encrypt_app():    
    layout = [[sg.Text('Select the files to encrypt')],
            [sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Encrypt Files', layout)
    event, values = window.Read()  
    x = values['_FILES_'].split(';')
    a = len(x)
    for i in range(a) :
        encrypted_file = encrypt.encrypt_file(i)
        os.path.join(vault_path)
    window.Close()

def decrypt_app():
    0