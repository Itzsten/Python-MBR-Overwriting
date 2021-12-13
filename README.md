# Python-MBR-Overwriting
A simple script to overwrite the MBR (Master Boot Record) using the Python coding language. This is only for educational purposes only, and I'm not responsible for any damage caused using this!

Libraries required: Pywin32

To overwrite it with custom hex, add a new line:
```python
data = bytes([ paste hex here... ])

WriteFile(hDevice, data, None)
```
