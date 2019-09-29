import PySimpleGUI as sg

layout = [[sg.Text('Enter 2 files to comare')],    
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