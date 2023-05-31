import struct
import os
from tkinter import filedialog
dats = filedialog.askopenfilenames()
for dat in dats:
    NAME = os.path.basename(dat).split(".")[0]
    out = os.getcwd()+"/output/"+NAME
    try:
        os.makedirs(out)
    except:
        ""
    f = open(dat,"r+b")
    print(dat)
    FINDS = [b'\x04\x02\x00\x04\x74\x43\x00\x00', # Tantalus Interactive
             ]
    TANT = b'art/'
    TANT2 = b'Art/'
    i = 0
    complete = 0
    CHECK = False
    for FIND in FINDS:
        f.seek(0)
        i = 0
        CHECK = False
        for B in range(os.path.getsize(dat)):
            A = f.read(1)
            if A[0] == FIND[i]:
                i+=1
                CHECK = True
                #print(i)
            if A[0] != FIND[i] and CHECK == False:
                i = 0
            CHECK = False
            if i == len(FIND)-1:
                f.seek(1,1)
                if complete == 0: #Figure out how filenames/paths are handled and implement them.
                    print("Tantalus Interactive")
                    print("Start of asset pointer table:",str(hex(struct.unpack("<I", f.read(4))[0]-0x08000000)))
                    f.seek(-4,1)
                    A = struct.unpack("<I", f.read(4))[0]-0x08000000
                    f.seek(A)
                    fileCount = struct.unpack("<I", f.read(4))[0]
                    f.seek(4,1)
                    FileTableOffset = f.tell()
                    f.seek(0)
                    for R in range(os.path.getsize(dat)):
                        DATACHECK1 = struct.unpack("<I", f.read(4))[0]-0x08000000
                        DCCNT = f.tell()
                        if DATACHECK1 > 0 and DATACHECK1 < 0x3FFFFF:
                            f.seek(DATACHECK1)
                            DATACHECK2 = struct.unpack("<I", f.read(4))[0]-0x08000000
                            #print(hex(DATACHECK2))
                            if DATACHECK2 > 0 and DATACHECK2 < 0x3FFFFF:
                                f.seek(DATACHECK2)
                                DATACHECK3 = struct.unpack("<I", f.read(4))[0]-0x08000000#f.read(4)
                                #print(DATACHECK3)
                                if DATACHECK3 > 0 and DATACHECK3 < 0x3FFFFF:
                                    DATACHECK4 = f.read(4)
                                    if DATACHECK4 == TANT or DATACHECK4 == TANT2:
                                        NAME = str("art/")
                                        L = 1
                                        while L != 0:
                                            L = f.read(1)[0]
                                            if L != 0:
                                                Letter = chr(L)
                                                NAME = str(NAME)+Letter
                                        print(NAME)
                        f.seek(DCCNT)
                    f.seek(FileTableOffset)
                    for ASSET in range(fileCount):
                        f.seek(4,1)
                        Offset = struct.unpack("<I", f.read(4))[0]-0x08000000
                        OLD = f.tell()
                        f.seek(Offset)
                        Length = struct.unpack("<I", f.read(4))[0]+4
                        f.seek(-4,1)
                        DAT = f.read(Length)
                        f.seek(OLD)
                        with open(out+f'/{ASSET}.rbh', "w+b") as outputFile:
                            outputFile.write(DAT)
                if complete == 1: #Reverse engineer another GBA game engine and put it here.
                    print("") 
                complete += 1 #Used to make it progress to the next one if there's more. If the next byte string isn't found, nothing happens.
                break
            

