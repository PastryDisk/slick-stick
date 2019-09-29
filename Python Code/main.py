import key_management, encrypt, setup
import sys, app

if(setup.setup_file != "1"):
    setup.setup()
    app.login()
else:
    app.login()
#What if you select two different drives by the USB location isn't a USB?
#What if someone changes the encrypted text in a file?
#Prompt user for password
#Select files to encrypt, what happens if not valid path?
#initialize_filepaths() is never called