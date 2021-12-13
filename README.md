# Python-MBR-Overwriting
A simple script to overwrite the MBR (Master Boot Record) using the Python coding language. This is only for educational purposes only, and I'm not responsible for any damage caused using this!

If you want to overwrite with Pywin32, then use Pywin32.py. If you prefer Ctypes, you may use ctypes.py.

To overwrite it with custom hex, add a new line:
```python
data = bytes([ paste hex here... ])

WriteFile(hDevice, data, None)
```
