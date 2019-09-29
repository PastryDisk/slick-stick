import key_management, encrypt, setup, app
import sys

#setup.setup()
app.app()

#What if you select two different drives by the USB location isn't a USB?
#What if someone changes the encrypted text in a file?
#Prompt user for password
#Select files to encrypt, what happens if not valid path?
#initialize_filepaths() is never called