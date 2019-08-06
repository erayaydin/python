import uuid
import os.path
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# PLEASE READ 'readme.txt' file

# Ask user for importing text (input or file)
def askForText():
    print("Get text from:")
    print("1) Input")
    print("2) File")

    choice = input("Choice: ")
    if choice == "1":
        text = input("Text: ")
    else:
        filename = input("Filename: ")
        f = open(filename, 'r')
        text = f.read()
        f.close()
    return text

# Padding text (for AES encryption)
def pad(s):
    return s + (32 - len(s) % 32) * chr(32 - len(s) % 32)

# Unpadding text (for AES decryption)
def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

# Encrypt text
def encrypt(plain):
    plain = pad(plain)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(hashlib.sha256("computer".encode()).digest(), AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain))

# Decrypt encrypted text
def decrypt(encrypted):
    enc = base64.b64decode(encrypted)
    iv = enc[:AES.block_size]
    cipher = AES.new(hashlib.sha256("computer".encode()).digest(), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

# Save text to file
def saveText(text, bytes = False, path = None):
    if path == None:
        path = str(uuid.uuid4())+".txt"
        if os.path.isfile(path):
            path = uuid.uuid4()+".txt"
    if bytes:
        f = open(path, 'w+b')
    else:
        f = open(path, 'w+')
    f.write(text)
    f.close()
    return path

quit = False
while not quit: # If user don't want to quit...

    # Get operation
    print("Please select an operation:")
    print("1) Encrypt a text")
    print("2) Decrypt a text")
    print("3) Exit")

    choice = input("Choice: ")
    if choice == "1": # Encrypt operation
        text = askForText() # Ask input from user
        encrypted = encrypt(text) # Encrypt text
        print("Encrypted Text:", encrypted) # Show encrypted text

        # Do you want save?
        isSave = input("Do you want to save encrypted text? (Y\\N)")
        if isSave == "Y" or isSave == "y":
            print("Save method:")
            print("1) Randomly create file")
            print("2) User defined location and filename")
            saveMethod = input("Choice: ")
            if saveMethod == "1": # Save randomly and assign path variable with location
                path = saveText(encrypted, True)
            else: # Save user defined location and assign path varaible with location
                saveLocation = input("Save location: ")
                path = saveText(encrypted, True, saveLocation)
            # Show location to user
            print("Encrypted text saved at",path)

    elif choice == "2": # Decrypt operation
        text = askForText()
        text = text.encode('utf-16')
        decrypted = decrypt(text)
        print("Decrypted Text:", decrypted)
        isSave = input("Do you want to save decrypted text? (Y\\N)")
        if isSave == "Y" or isSave == "y":
            print("Save method:")
            print("1) Randomly create file")
            print("2) User defined location and filename")
            saveMethod = input("Choice: ")
            if saveMethod == "1":
                path = saveText(decrypted)
            else:
                saveLocation = input("Save location: ")
                path = saveText(decrypted, False, saveLocation)
            print("Decrypted text saved at", path)
    elif choice == "3": # User wants to quit from app
        quit = True