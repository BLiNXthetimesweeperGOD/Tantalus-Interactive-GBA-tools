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
def checkForByteString(path, string):
    with open(path, 'rb') as file:
        content = file.read()
        offset = content.find(string)
        return string in content, offset

file = openFile()
outPath = os.getcwd()+"/"+os.path.splitext(os.path.basename(file))[0]
if not os.path.exists(outPath):
    os.makedirs(outPath)

found, offset = checkForByteString(file, b'\x04\x02\x00\x04\x74\x43\x00\x00')

if found == True: #The ROM contained the byte string. Start extracting files.
    with open(file, "rb") as rom:
        rom.seek(offset+8)
        tableOffset = uintPointer(rom.read(4))
        fileTableRootPathOffset = uintPointer(rom.read(4)) #If filenames ever get implemented, this is effectively the root of the ROM ("../targ/")
        rom.seek(tableOffset)
        fileCount = uint(rom.read(4))
        fileTableVersion = uint(rom.read(4)) #Just a guess - this could be something else entirely, but I have no idea yet
        for asset in range(fileCount):
            fileNameHash = uint(rom.read(4)) #This is calculated and stored in register 7 until the correct file in the file table has been found.
            fileOffset = uintPointer(rom.read(4))
            savedPosition = rom.tell()
            rom.seek(fileOffset)
            fileSize = uint(rom.read(4))
            with open(outPath+f"/{asset}.rbh", "w+b") as outputFile:
                outputFile.write(rom.read(fileSize))
            rom.seek(savedPosition)
else:
    print("The ROM you ran this on is not a valid Tantalus Interactive GBA game.\nThis could be because it's a bad dump, not a ROM or a game from a different developer.\nPress enter/return to close this window.")
    input() #Actually give the user the ability to read this if ran normally
