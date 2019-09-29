import PySimpleGUI as sg
import encrypt
import os.path

layout = [[sg.Image("C:/Users/kmasi/Desktop/logo.png")],
         [sg.Text('Select 2 files to compare')],    
         [sg.Text('Vault Location', size=(10, 1)), sg.Input(), sg.FolderBrowse()],      
         [sg.Text('USB Location', size=(10, 1)), sg.Input(), sg.FolderBrowse()],      
         [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Initial Setup', layout)  

event, values = window.Read()  
window.Close()

vault_filename = values[0]
USB_filename = values[1]

print(vault_filename)
print(USB_filename)

if(vault_filename != USB_filename) :
    layout = [[sg.Text('Select the files to encrypt')],
         [sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Initial Setup', layout)
    event, values = window.Read()  
    x = values['_FILES_'].split(';')
    a = len(x)
    for i in range(a) :
        encrypted_file = encrypt.encrypt_file(i)
        os.path.join(vault_filename)
        #Error for me. Do not have masterkey.txt
    window.Close()