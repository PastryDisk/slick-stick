import PySimpleGUI as sg
import encrypt, key_management
import os.path

def setup():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'logo.png')

    layout = [[sg.Image(filename)],
             [sg.Text('Select 2 different directories')],    
             [sg.Text('Vault Location', size=(10, 1)), sg.Input(), sg.FolderBrowse()],      
             [sg.Text('USB Location', size=(10, 1)), sg.Input(), sg.FolderBrowse()],      
             [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Initial Setup', layout)  

    event, values = window.Read()  

    vault_filename = values[1]
    USB_filename = values[2]

    window.Close()

    if(os.path.isdir(vault_filename) and os.path.isdir(USB_filename)):
        if(vault_filename[:1] != USB_filename[:1]) :
            i = 1
            l = 1
            while (i == l):
                vaultpath = os.path.join(dirname, 'vaultfilepath.txt') 
                USBpath = os.path.join(dirname, 'USBfilepath.txt')
                with open(vaultpath, 'wb') as f:
                    f.write(vault_filename.encode("utf-8"))
                with open(USBpath, 'wb') as f:
                    f.write(USB_filename.encode("utf-8"))
                
                layout = [[sg.Image(filename)],
                    [sg.Text('Create a password')],    
                    [sg.Text('Password', size=(10, 1)), sg.Input(password_char="*")],      
                    [sg.Text('Re-enter Password', size=(10, 1)), sg.Input(password_char="*")],      
                    [sg.Submit(), sg.Cancel()]]      

                window = sg.Window('Initial Setup', layout)  

                event, values = window.Read()  

                password1 = values[1]
                password2 = values[2]

                window.Close()

                
                if (password1 == password2):
                    key_management.create_passwd(password1, (USB_filename + "/password.txt"))
                    key_management.generate_file_key(USB_filename + "/key.txt")
                    i = 2
                else:
                    layout = [[sg.Image(filename)],
                            [sg.Text('Please enter the same password in both fields')],       
                            [sg.Ok()]]     

                    window = sg.Window('Initial Setup', layout)  

                    event, values = window.Read() 
                    window.Close() 
        else:
            layout = [[sg.Image(filename)],
                [sg.Text('You have selected filepaths on the same drive. Please select filepaths on two different drives.')],       
                [sg.Button(button_text="Reset")]]      

            window = sg.Window('Initial Setup', layout)  

            event, values = window.Read() 
            window.Close() 

            if event == 'Reset':
                setup()
    else: 
        layout = [[sg.Image(filename)],
            [sg.Text('One or more directories is invalid. Please Select valid directories.')],       
            [sg.Button(button_text="Reset")]]      

        window = sg.Window('Initial Setup', layout)  

        event, values = window.Read() 
        window.Close() 

        if event == 'Reset':
            setup()