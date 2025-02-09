#Tantalus Interactive ROM extractor redo
import os
from filenamelists import *

#Functions were moved to another script to make altering the main one easier
from helperFunctions import *

#Format = game name, engine version, fileTableEntry variable
gameIDs = [[b'WWCC5', 0, 1],
           [b'ATV QUAD POW', 0, 0],
           [b'MTM', 1, 0],
           [b'TGRALLY', 1, 0],
           [b'JIMMYNEUAOTT', 1, 0],
           [b'POLAREXPRESS', 1, 0],
           [b'TSTAR', 1, 0],
           [b'CARSMATER', 1, 0]]

def getSetupVariables(file):
    targs = [b'targ/', b'../targ/']
    with open(file, 'rb') as gba:
        gba.seek(0xA0)
        nameBytes = gba.read(0xC)
        for game in gameIDs:
            if nameBytes.startswith(game[0]):
                return targs[game[1]], game[2], True
    return 0, 0, False

file = openFile()

outputFolder = os.getcwd()+"/extracted/"+os.path.splitext(os.path.basename(file))[0]+"/"

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

filenameList = []
targ, fileTableEntry, isTantalusROM = getSetupVariables(file)
if targ == b'../targ/':
    filenameList.extend(filenameListLaterGames())
if targ == b'targ/':
    filenameList.extend(filenameListEarlierGames())
filenameList.extend(extendNameList(file))
foundStatus, offset = checkForByteString(file, b'\x04\x02\x00\x04\x74\x43\x00\x00')

if foundStatus == True and isTantalusROM == True:
    with open(file, 'rb') as rom:
        rom.seek(offset+8)
        tableOffset = uintPointer(rom.read(4))
        rom.seek(tableOffset)
        fileCount = uint(rom.read(4))
        fileTableVersion = uint(rom.read(4))
        for asset in range(fileCount):
            fileIdentifier = uint(rom.read(4)) #Was referred to as a hash in the old script
            for filename in filenameList:
                if targ == b'targ/':
                    generatedIdentifier = generateIdentifierOld(targ+filename, fileTableEntry)
                elif targ == b'../targ/':
                    generatedIdentifier = generateIdentifier(targ+filename, fileTableEntry)
                
                if fileIdentifier == generatedIdentifier:
                    outputName = outputFolder+filename[0:-1].decode("utf-8")
                    path = os.path.dirname(outputName)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    data = getFileData(file, uintPointer(rom.read(4)))
                    with open(outputName, "w+b") as outputFile:
                        outputFile.write(data)

                    break
            if fileIdentifier != generatedIdentifier: #No filename was found in the list - write as-is
                outputName = outputFolder+f'NONAME/{asset:03d}.rbh'
                path = os.path.dirname(outputName)
                if not os.path.exists(path):
                    os.makedirs(path)
                data = getFileData(file, uintPointer(rom.read(4)))
                with open(outputName, "w+b") as outputFile:
                    outputFile.write(data)
