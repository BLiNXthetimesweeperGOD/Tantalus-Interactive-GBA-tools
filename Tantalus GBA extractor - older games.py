#Tantalus Interactive GBA file extractor
import os
import tkinter as tk
from tkinter import filedialog
import struct

def makeCharacterUppercase(character):
    if character - 0x61 < 0x1A:
        character = character - 0x20
    return character

def generateFilenameHash(string, entryZero):
    weightedSum = 1
    index = 0
    characterOffset = 0
    character = string[index]
    while character != 0x00:
        if character not in range(0x20, 0x2F) and character not in range(0x5B, 0x61) and character != 0x2F and character != 0x5C:
            processedCharacter = makeCharacterUppercase(character)
            processedCharacter &= 0xFF
        else:
            processedCharacter = character
        if character == 0x2F:
            processedCharacter = 0x5C
        weightedSum = weightedSum + processedCharacter * (index + entryZero)
        index += 1
        character = string[index]
    return weightedSum

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
def getZeroTerminatedString(file, offset):
    string = b""
    scan = b''
    with open(file, "rb") as fileWithString:
        fileWithString.seek(offset)
        while scan != b'\x00':
            scan = fileWithString.read(1)
            if scan != b'\x00':
                string += scan
    return string
def findStrings(filePath, byteString):
    results = []
    with open(filePath, "rb") as file:
        content = file.read()
        start = 0
        while True:
            start = content.find(byteString, start)
            if start == -1:
                break
            string = getZeroTerminatedString(filePath, start)
            results.append(b'targ/'+string + b'\x00')
            start += len(byteString)
    return results

file = openFile()

#Grab all filenames from the ROM for later use
fileNameList = []
fileNameList.extend(findStrings(file, b'art/'))
fileNameList.extend(findStrings(file, b'Art/'))
fileNameList.extend(findStrings(file, b'ART/'))

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
            named = False
            fileNameHash = uint(rom.read(4)) #This is calculated and stored in register 7 until the correct file in the file table has been found.
            for fileName in fileNameList:
                Hash = generateFilenameHash(fileName, 0)
                if Hash == fileNameHash:
                    outName = fileName[0:-1].decode('UTF-8')
                    subOutPath = os.path.dirname(outName)
                    if not os.path.exists(outPath+"/"+subOutPath):
                        os.makedirs(outPath+"/"+subOutPath)
                    named = True
                    break
            fileOffset = uintPointer(rom.read(4))
            savedPosition = rom.tell()
            rom.seek(fileOffset)
            fileSize = uint(rom.read(4))
            if named == True:
                with open(outPath+f"/{outName}", "w+b") as outputFile:
                    outputFile.write(rom.read(fileSize))
            rom.seek(savedPosition)
else:
    print("The ROM you ran this on is not a valid Tantalus Interactive GBA game.\nThis could be because it's a bad dump, not a ROM or a game from a different developer.\nPress enter/return to close this window.")
    input() #Actually give the user the ability to read this if ran normally
