from helperFunctions import *
#Filenames with %s in them can't be grabbed by the script currently.
#I've filled in most of the missing names here.
def extendNameList(file):
    filenameList = []
    filenameList.extend(findStrings(file, b'art/'))
    filenameList.extend(findStrings(file, b'Art/'))
    filenameList.extend(findStrings(file, b'ART/'))
    return filenameList

def generateListOfWoodyWoodpeckerAssets():
    stageList = []
    worlds = ['wind', 'sand', 'wood', 'water', 'fire', 'fairy']
    characters = ["vinerope", "angelfish", "Anglerfish", "blowflower", "bombrock", "bottleopener", "catintrashcan", "electriccloud", "fireflower",
                  "firemole", "flowerpowerplant", "flyingturtle", "goldenbat", "handhead", "hellcat", "hotdog", "jetcuctus", "killercone", "licker",
                  "madfly", "minimothra", "monsterkito", "monsterteddy", "mummy", "mushroomman", "pearlinmussel", "pekingduck", "pinocchio", "popcorn",
                  "razorfly", "scarfbird", "Skeletonfish", "spideeeeer", "starman", "Stonecrab", "venusflytrap", "violentsnake", "walkingplant",
                  "windgenie", "giant_mummy", "giantplant", "squid", "clown", "finaldoor", "crate", "Stonecrate", "Metalcrate", "Jarcrate",
                  "Meringue", "boulder", "waterfall", "steam", "lamp", "eruption", "piston", "switch", "clouds", "leaf", "whizzer"]
    
    for character in characters:
        asset = str('art/characters/%s/char.rbh' % (character)).encode("utf-8")+b'\x00'
        stageList.append(asset)
    for world in worlds:
        resources = str('art/worlds/%s0/resc.rbh' % (world)).encode("utf-8")+b'\x00'
        generalCharacterSet = str('art/worlds/%s0/gcset.rbh' % (world)).encode("utf-8")+b'\x00'
        woody =  str('art/characters/woody/skel%s.rbh' % (world)).encode("utf-8")+b'\x00'
        stageList.extend([resources, generalCharacterSet, woody])
    for room in range(50):
        stage = str('art/worlds/tr_room0%d/world.rbh' % (room)).encode("utf-8")+b'\x00'
        stageList.append(stage)
    for screen in range(50):
        asset = str('art/screens/congrat/data%d.rbh' % (screen)).encode("utf-8")+b'\x00'
        stageList.append(asset)
    for world in worlds:
        for room in range(50):
            stage = str('art/worlds/%s%d/world.rbh' % (world, room)).encode("utf-8")+b'\x00'
            stageList.append(stage)
    return stageList
def filenameListEarlierGames():
    filenameList = generateListOfWoodyWoodpeckerAssets()
    return filenameList
def filenameListLaterGames():
    filenameList = [
                    b'art/cars/LightningMcQueen/spritetemplate.rbh\x00',
                    b'art/cars/LightningMcQueen/car.rbh\x00',
                    b'art/cars/McQueen/spritetemplate.rbh\x00',
                    b'art/cars/McQueen/car.rbh\x00',
                    b'art/cars/ramone/spritetemplate.rbh\x00',
                    b'art/cars/ramone/car.rbh\x00',
                    b'art/cars/sheriff/spritetemplate.rbh\x00',
                    b'art/cars/sheriff/car.rbh\x00',
                    b'art/cars/luigi/spritetemplate.rbh\x00',
                    b'art/cars/luigi/car.rbh\x00',
                    b'art/cars/mater/spritetemplate.rbh\x00',
                    b'art/cars/mater/car.rbh\x00',
                    b'art/cars/sarge/spritetemplate.rbh\x00',
                    b'art/cars/sarge/car.rbh\x00',
                    b'art/cars/lizzie/spritetemplate.rbh\x00',
                    b'art/cars/lizzie/car.rbh\x00',
                    b'art/cars/doc/spritetemplate.rbh\x00',
                    b'art/cars/doc/car.rbh\x00',
                    b'art/cars/otto/spritetemplate.rbh\x00',
                    b'art/cars/otto/car.rbh\x00',
                    b'art/cars/sven/spritetemplate.rbh\x00',
                    b'art/cars/sven/car.rbh\x00',
                    b'art/cars/emma/spritetemplate.rbh\x00',
                    b'art/cars/emma/car.rbh\x00',
                    b'art/cars/hiro/spritetemplate.rbh\x00',
                    b'art/cars/hiro/car.rbh\x00',
                    b'art/cars/giovanni/spritetemplate.rbh\x00',
                    b'art/cars/giovanni/car.rbh\x00',
                    b'art/cars/car00/spritetemplate.rbh\x00',
                    b'art/cars/car01/spritetemplate.rbh\x00',
                    b'art/cars/car02/spritetemplate.rbh\x00',
                    b'art/cars/car03/spritetemplate.rbh\x00',
                    b'art/cars/car04/spritetemplate.rbh\x00',
                    b'art/cars/car05/spritetemplate.rbh\x00',
                    b'art/cars/car06/spritetemplate.rbh\x00',
                    b'art/cars/car07/spritetemplate.rbh\x00',
                    b'art/cars/car08/spritetemplate.rbh\x00',
                    b'art/cars/car09/spritetemplate.rbh\x00',
                    b'art/cars/car10/spritetemplate.rbh\x00',
                    b'art/cars/car11/spritetemplate.rbh\x00',
                    b'art/cars/car12/spritetemplate.rbh\x00',
                    b'art/cars/car13/spritetemplate.rbh\x00',
                    b'art/cars/car14/spritetemplate.rbh\x00',
                    b'art/cars/car15/spritetemplate.rbh\x00',
                    b'art/cars/car16/spritetemplate.rbh\x00',
                    b'art/cars/car17/spritetemplate.rbh\x00',
                    b'art/cars/car18/spritetemplate.rbh\x00',
                    b'art/cars/car19/spritetemplate.rbh\x00',
                    b'art/cars/car20/spritetemplate.rbh\x00',
                    b'art/cars/car00/car.rbh\x00',
                    b'art/cars/car01/car.rbh\x00',
                    b'art/cars/car02/car.rbh\x00',
                    b'art/cars/car03/car.rbh\x00',
                    b'art/cars/car04/car.rbh\x00',
                    b'art/cars/car05/car.rbh\x00',
                    b'art/cars/car06/car.rbh\x00',
                    b'art/cars/car07/car.rbh\x00',
                    b'art/cars/car08/car.rbh\x00',
                    b'art/cars/car09/car.rbh\x00',
                    b'art/cars/car10/car.rbh\x00',
                    b'art/cars/car11/car.rbh\x00',
                    b'art/cars/car12/car.rbh\x00',
                    b'art/cars/car13/car.rbh\x00',
                    b'art/cars/car14/car.rbh\x00',
                    b'art/cars/car15/car.rbh\x00',
                    b'art/cars/car16/car.rbh\x00',
                    b'art/cars/car17/car.rbh\x00',
                    b'art/cars/car18/car.rbh\x00',
                    b'art/cars/car19/car.rbh\x00',
                    b'art/cars/car20/car.rbh\x00',
                    b'Art/Fonts/Sylfaen.rbh\x00',
                    b'Art/Fonts/Sylfaen15.rbh\x00',
                    b'Art/Fonts/Sylfaen_VRAM.rbh\x00',
                    b'Art/Fonts/Sylfaen15_VRAM.rbh\x00'
                    ]
    return filenameList
