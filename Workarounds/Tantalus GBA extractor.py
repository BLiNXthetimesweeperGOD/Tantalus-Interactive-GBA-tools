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
    hashRegister = 1
    weightedSum = 1
    index = 0
    character = string[index]
    while character != 0x00:
        if character not in range(0, 0x61):
            processedCharacter = makeCharacterUppercase(character)
        else:
            processedCharacter = character
        if character == 0x2F:
            processedCharacter = 0x5C

        weightedSum = weightedSum + processedCharacter * (index + entryZero)
        hashRegister = (hashRegister * 2) + weightedSum
        hashRegister = hashRegister & 0xFFFFFFFF
        character = string[index]
        if index == 1:
            hashRegister -= 4
        index += 1
    return hashRegister, weightedSum


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
            results.append(string + b'\x00')
            start += len(byteString)
    return results

file = openFile()
cars = [b"LightningMcQueen"]
#Grab all filenames from the ROM for later use
fileNameList = [b"art/cars/LightningMcQueen/spritetemplate.rbh\x00",
                b"art/cars/LightningMcQueen/car.rbh\x00",
                b"art/cars/McQueen/spritetemplate.rbh\x00",
                b"art/cars/McQueen/car.rbh\x00",
                b"art/cars/ramone/spritetemplate.rbh\x00",
                b"art/cars/ramone/car.rbh\x00",
                b"art/cars/sheriff/spritetemplate.rbh\x00",
                b"art/cars/sheriff/car.rbh\x00",
                b"art/cars/luigi/spritetemplate.rbh\x00",
                b"art/cars/luigi/car.rbh\x00",
                b"art/cars/mater/spritetemplate.rbh\x00",
                b"art/cars/mater/car.rbh\x00",
                b"art/cars/sarge/spritetemplate.rbh\x00",
                b"art/cars/sarge/car.rbh\x00",
                b"art/cars/lizzie/spritetemplate.rbh\x00",
                b"art/cars/lizzie/car.rbh\x00",
                b"art/cars/doc/spritetemplate.rbh\x00",
                b"art/cars/doc/car.rbh\x00",
                b"art/cars/otto/spritetemplate.rbh\x00",
                b"art/cars/otto/car.rbh\x00",
                b"art/cars/sven/spritetemplate.rbh\x00",
                b"art/cars/sven/car.rbh\x00",
                b"art/cars/emma/spritetemplate.rbh\x00",
                b"art/cars/emma/car.rbh\x00",
                b"art/cars/hiro/spritetemplate.rbh\x00",
                b"art/cars/hiro/car.rbh\x00",
                b"art/cars/giovanni/spritetemplate.rbh\x00",
                b"art/cars/giovanni/car.rbh\x00",
                b"art/cars/car00/spritetemplate.rbh\x00",
                b"art/cars/car01/spritetemplate.rbh\x00",
                b"art/cars/car02/spritetemplate.rbh\x00",
                b"art/cars/car03/spritetemplate.rbh\x00",
                b"art/cars/car04/spritetemplate.rbh\x00",
                b"art/cars/car05/spritetemplate.rbh\x00",
                b"art/cars/car06/spritetemplate.rbh\x00",
                b"art/cars/car07/spritetemplate.rbh\x00",
                b"art/cars/car08/spritetemplate.rbh\x00",
                b"art/cars/car09/spritetemplate.rbh\x00",
                b"art/cars/car10/spritetemplate.rbh\x00",
                b"art/cars/car11/spritetemplate.rbh\x00",
                b"art/cars/car12/spritetemplate.rbh\x00",
                b"art/cars/car13/spritetemplate.rbh\x00",
                b"art/cars/car14/spritetemplate.rbh\x00",
                b"art/cars/car15/spritetemplate.rbh\x00",
                b"art/cars/car16/spritetemplate.rbh\x00",
                b"art/cars/car17/spritetemplate.rbh\x00",
                b"art/cars/car18/spritetemplate.rbh\x00",
                b"art/cars/car19/spritetemplate.rbh\x00",
                b"art/cars/car20/spritetemplate.rbh\x00",
                b"art/cars/car00/car.rbh\x00",
                b"art/cars/car01/car.rbh\x00",
                b"art/cars/car02/car.rbh\x00",
                b"art/cars/car03/car.rbh\x00",
                b"art/cars/car04/car.rbh\x00",
                b"art/cars/car05/car.rbh\x00",
                b"art/cars/car06/car.rbh\x00",
                b"art/cars/car07/car.rbh\x00",
                b"art/cars/car08/car.rbh\x00",
                b"art/cars/car09/car.rbh\x00",
                b"art/cars/car10/car.rbh\x00",
                b"art/cars/car11/car.rbh\x00",
                b"art/cars/car12/car.rbh\x00",
                b"art/cars/car13/car.rbh\x00",
                b"art/cars/car14/car.rbh\x00",
                b"art/cars/car15/car.rbh\x00",
                b"art/cars/car16/car.rbh\x00",
                b"art/cars/car17/car.rbh\x00",
                b"art/cars/car18/car.rbh\x00",
                b"art/cars/car19/car.rbh\x00",
                b"art/cars/car20/car.rbh\x00"
                ]
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
        fileTableRootPathOffset = uintPointer(rom.read(4)) #This is effectively the root of the ROM ("../targ/")
        print(hex(offset))
        rom.seek(tableOffset)
        fileCount = uint(rom.read(4))
        fileTableVersion = uint(rom.read(4)) #Just a guess - this could be something else entirely, but I have no idea yet
        for asset in range(fileCount):
            named = False
            fileNameHash = uint(rom.read(4)) #This is calculated and stored in register 7 until the correct file in the file table has been found.
            for fileName in fileNameList:
                #The games check both the base string and the string with "../targ/" added to them
                Hash, Sum = generateFilenameHash(fileName, 0)
                if Hash == fileNameHash:
                    outName = '/targ/'+fileName.decode('UTF-8')
                    subOutPath = os.path.dirname(outName)
                    if not os.path.exists(outPath+"/targ/"+subOutPath):
                        os.makedirs(outPath+"/targ/"+subOutPath)
                    named = True
                    break
                elif Sum == fileNameHash:
                    outName = '/targ/'+fileName.decode('UTF-8')
                    subOutPath = os.path.dirname(outName)
                    if not os.path.exists(outPath+"/targ/"+subOutPath):
                        os.makedirs(outPath+"/targ/"+subOutPath)
                    named = True
                    break
                Hash, Sum = generateFilenameHash(b'../targ/'+fileName, 0)
                if Hash == fileNameHash and named == False:
                    outName = b'../targ/'+fileName
                    outName = outName.decode('UTF-8')[3:-1]
                    subOutPath = os.path.dirname(outName)
                    if not os.path.exists(outPath+"/"+subOutPath):
                        os.makedirs(outPath+"/"+subOutPath)
                    named = True
                    break
                if Sum == fileNameHash and named == False:
                    outName = b'../targ/'+fileName
                    outName = outName.decode('UTF-8')[3:-1]
                    subOutPath = os.path.dirname(outName)
                    if not os.path.exists(outPath+"/"+subOutPath):
                        os.makedirs(outPath+"/"+subOutPath)
                    named = True
                    break
                if named == False:
                    if not os.path.exists(outPath+"/targ/"):
                        os.makedirs(outPath+"/targ/")
            fileOffset = uintPointer(rom.read(4))
            savedPosition = rom.tell()
            rom.seek(fileOffset)
            fileSize = uint(rom.read(4))
            if named == True:
                with open(outPath+f"/{outName}", "w+b") as outputFile:
                    outputFile.write(rom.read(fileSize))
            else:
                with open(outPath+f"/targ/FAILEDTOFINDNAME_{asset}.rbh", "w+b") as outputFile:
                    outputFile.write(rom.read(fileSize))
            rom.seek(savedPosition)
else:
    print("The ROM you ran this on is not a valid Tantalus Interactive GBA game.\nThis could be because it's a bad dump, not a ROM or a game from a different developer.\nPress enter/return to close this window.")
    input() #Actually give the user the ability to read this if ran normally
