import os
import sys

if os.environ['PATH'].lower().find('python') != -1:
    print("Python is in PATH. Script will be executed correctly.")
    in_path = True
else:
    print("Python is not in PATH. Pls specify the PATH of python: ")
    in_path = False
    py_path = input()
    try:
        os.system(f"{py_path} -V")
    except:
        print("Incorrect PATH.")
        exit()

print("The libs necessary to run bot.py will now be downloaded...")

if in_path == True:
    if sys.platform == "win32":
        py_path = "python"
    else:
        py_path = "python3"
os.system(f"{py_path} -m pip install --upgrade pip") # Upgrade before installing anything
os.system(f"{py_path} -m pip install -r install/requirements.txt") # install bot packages

print("Installation finished.")
