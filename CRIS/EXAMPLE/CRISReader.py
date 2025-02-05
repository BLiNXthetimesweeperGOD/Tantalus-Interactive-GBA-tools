from codingTools import *
#Tantalus Interactive CRIS engine mesh reader
def getQuadBit(quadValue): #0 = tri, 1 = quad
    return (quadValue >> 3) & 1
def getFacesAndUVs(file, count):
    faces = []
    for face in range(count):
        unknown = file.read(3)
        isQuad = getQuadBit(file.read(1)[0])
        index1, index2, index3, index4 = file.read(4)
        if isQuad == 1:
            faces.append([index1, index2, index3, index4])
            #Skip extra data for now (formatting isn't known)
            file.seek(8, 1)
        else:
            faces.append([index1, index2, index3])
            #Skip extra data for now (formatting isn't known)
            file.seek(0xC, 1)
    return faces, None

def getVertices(file, count): #Pass an already opened file to this and it should read the vertices
    vertices = []
    for vertex in range(count):
        x = unpack.short(file.read(2))
        y = unpack.short(file.read(2))
        z = unpack.short(file.read(2))
        padding = file.read(2)
        vertices.append([x, y, z])
    return vertices

def convertVerticesToOBJVertices(vertices):
    lines = ""
    for vertex in vertices:
        converted = f'v {vertex[0]} {vertex[1]} {vertex[2]}\n'
        lines += converted
    return lines

#TO-DO: Figure out the UV formatting and write a function for converting them.
#They seem to be non-standard/proprietary in how they work.
#Weights aren't supported by OBJ, so a function for them should still be added but only as documentation

def convertFacesToOBJFaces(faces):
    lines = ""
    for face in faces:
        if len(face) < 4:
            converted = f'f {face[0]+1} {face[1]+1} {face[2]+1}\n'
        else:
            converted = f'f {face[0]+1} {face[1]+1} {face[2]+1} {face[3]+1}\n'
        lines += converted
    return lines

rbh = dialogs.file()
with open(rbh, "rb") as file:
    #Actual RBH decoding is needed. These values only work for art/vehicles/theboy.rbh from The Polar Express after it has been decompressed.
    file.seek(0x111C)
    faces, uvs = getFacesAndUVs(file, 220)
    file.seek(0x1F38)
    vertices = getVertices(file, 212)
    convertedVertices = convertVerticesToOBJVertices(vertices)
    convertedFaces = convertFacesToOBJFaces(faces)
    with open("TEST.obj", "w+") as output:
        output.write(convertedVertices)
        output.write(convertedFaces)
    
