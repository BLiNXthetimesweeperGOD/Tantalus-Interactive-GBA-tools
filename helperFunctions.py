import os
import tkinter as tk
from tkinter import filedialog
import struct
import filenamelists
def openFile():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename()
    root.destroy()
    return file
def uint(data):
    return struct.unpack("<I", data)[0]
def uintPointer(data):
    return struct.unpack("<I", data)[0]-0x08000000
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
def getFileData(filePath, offset):
    with open(filePath, "rb") as rom:
        rom.seek(offset)
        size = uint(rom.read(4))
        return rom.read(size)

def makeCharacterUppercase(character):
    if character - 0x61 < 0x1A:
        character = character - 0x20
    return character

def generateIdentifierOld(string, entryZero):
    weightedSum = 1
    index = 0
    character = string[index]
    while character != 0x00:
        if character not in range(0, 0x61):
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

def generateIdentifier(string, entryZero):
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
    return hashRegister
