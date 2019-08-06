from Crypto.Cipher import AES
import base64
from datetime import datetime

while True:
    op = input("(E)ncrypt or (D)crypt")

    pad = lambda s: s + (32 - len(s) % 32) * '{'
    encode = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    decode = lambda c, e: c.decrypt(base64.b64decode(e))
    cipher = AES.new("1234567890123456")
    if op == "E" or op == "e":
        filepath = input("Plain text filename: ")
        f = open(filepath, 'r')
        text = f.read()
        f.close()
        encoded = encode(cipher, text)
        filename = str(datetime.now())+"-encrypted.txt"
        w = open(filename, "w+b")
        w.write(encoded)
        w.close()
        print(text+" encrypted and saved at "+filename)
    elif op == "D" or op == "d":
        filepath = input("Encrypted text filename: ")
        f = open(filepath, 'rb')
        text = f.read()
        f.close()
        decoded = decode(cipher, text)
        decoded = decoded.decode().rstrip('{')
        filename = str(datetime.now())+"-decrypted.txt"
        w = open(filename, "w+")
        w.write(decoded)
        w.close()
        print(str(text)+" decrypted and saved at "+filename)

    quit = input("Do you want exit ? (Y)es or (N)o")
    if quit == "Y":
        break