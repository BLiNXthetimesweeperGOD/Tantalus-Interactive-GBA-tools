#Tantalus Interactive GBA file extractor
import os
import tkinter as tk
from tkinter import filedialog
import struct

def uint(data):
    return struct.unpack("<I", data)[0]
def uintPointer(data):
    return struct.unpack("<I", data)[0]-0x08000000

def openFile():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename()
    root.destroy()
    return file

file = openFile()
outPath = os.getcwd()+"/"+os.path.splitext(os.path.basename(file))[0]
if not os.path.exists(outPath):
    os.makedirs(outPath)

def checkForByteString(path, string):
    with open(path, 'rb') as file:
        content = file.read()
        offset = content.find(string)
        return string in content, offset

found, offset = checkForByteString(file, b'\x04\x02\x00\x04\x74\x43\x00\x00')

if found == True:
    with open(file, "rb") as rom:
        rom.seek(offset+8)
        tableOffset = uintPointer(rom.read(4))
        rom.seek(tableOffset)
        fileCount = uint(rom.read(4))
        rom.seek(4, 1)
        for asset in range(fileCount):
            rom.seek(4, 1)
            fileOffset = uintPointer(rom.read(4))
            savedPosition = rom.tell()
            rom.seek(fileOffset)
            fileSize = uint(rom.read(4))
            with open(outPath+f"/{asset}.rbh", "w+b") as outputFile:
                outputFile.write(rom.read(fileSize))
            rom.seek(savedPosition)
else:
    print("This ROM is either not from Tantalus Interactive or a bad dump.\nPress enter/return to close this window.")
    input() #Actually give the user the ability to read this if ran normally
