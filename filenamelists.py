from helperFunctions import *
#Filenames with %s in them can't be grabbed by the script currently.
#I've filled in most of the missing names here.
def extendNameList(file):
    filenameList = []
    filenameList.extend(findStrings(file, b'art/'))
    filenameList.extend(findStrings(file, b'Art/'))
    filenameList.extend(findStrings(file, b'ART/'))
    return filenameList

def generateListOfNewerGameAssets(): #The massive list in filenameListLaterGames needs to go.
    assets = []
    worlds = []
    characters = ['LightningMcQueen', 'ramone', 'sheriff', 'luigi', 'mater', 'sarge', 'lizzie', 'doc', 'otto', 'sven', 'emma', 'hiro', 'giovanni',
                  'bearclaw', 'anaconda', 'bulldozer', 'cadillac', 'carnivore', 'drone', 'executioner', 'grave_digger', 'mack', 'monster_patrol',
                  'nitemare', 'scorpion', 'carolina_crusher', 'vw_van', 'chook']
    tracks = ['archdig', 'beach', 'city', 'docklands', 'greenhills', 'junkyard', 'raceway', 'ski', 'stadium', 'thewest']
    for character in characters:
        car1 = str('art/cars/%s/spritetemplate.rbh' % (character)).encode("utf-8")+b'\x00'
        car2 = str('art/cars/%s/car.rbh' % (character)).encode("utf-8")+b'\x00'
        car3 = str('art/vehicles/%s/spritetemplate.rbh' % (character)).encode("utf-8")+b'\x00'
        car4 = str('art/vehicles/%s/car.rbh' % (character)).encode("utf-8")+b'\x00'
        assets.extend([car1, car2, car3, car4])
    for ID in range(20):
        car = str(f'art/cars/car{ID:02d}/car.rbh').encode("utf-8")+b'\x00'
        spritetemplate = str(f'art/cars/car{ID:02d}/spritetemplate.rbh').encode("utf-8")+b'\x00'
        assets.extend([car, spritetemplate])
    for track in tracks:
        for ID in range(10):
            trackdef = str('art/tracks/%s/trackdef%d.rbh' % (track, ID)).encode("utf-8")+b'\x00'
            assets.append(trackdef)
        track = str('art/tracks/%s/track.rbh' % (track)).encode("utf-8")+b'\x00'
        charset = str('art/tracks/%s/charset.rbh' % (track)).encode("utf-8")+b'\x00'
        assets.extend([track, charset])
    return assets

def generateListOfWoodyWoodpeckerAssets():
    assets = []
    worlds = ['wind', 'sand', 'wood', 'water', 'fire', 'fairy']
    characters = ["vinerope", "angelfish", "Anglerfish", "blowflower", "bombrock", "bottleopener", "catintrashcan", "electriccloud", "fireflower",
                  "firemole", "flowerpowerplant", "flyingturtle", "goldenbat", "handhead", "hellcat", "hotdog", "jetcuctus", "killercone", "licker",
                  "madfly", "minimothra", "monsterkito", "monsterteddy", "mummy", "mushroomman", "pearlinmussel", "pekingduck", "pinocchio", "popcorn",
                  "razorfly", "scarfbird", "Skeletonfish", "spideeeeer", "starman", "Stonecrab", "venusflytrap", "violentsnake", "walkingplant",
                  "windgenie", "giant_mummy", "giantplant", "squid", "clown", "finaldoor", "crate", "Stonecrate", "Metalcrate", "Jarcrate",
                  "Meringue", "boulder", "waterfall", "steam", "lamp", "eruption", "piston", "switch", "clouds", "leaf", "whizzer"]
    
    for character in characters:
        asset = str('art/characters/%s/char.rbh' % (character)).encode("utf-8")+b'\x00'
        assets.append(asset)
    for world in worlds:
        resources = str('art/worlds/%s0/resc.rbh' % (world)).encode("utf-8")+b'\x00'
        generalCharacterSet = str('art/worlds/%s0/gcset.rbh' % (world)).encode("utf-8")+b'\x00'
        woody =  str('art/characters/woody/skel%s.rbh' % (world)).encode("utf-8")+b'\x00'
        assets.extend([resources, generalCharacterSet, woody])
    for room in range(50):
        stage = str('art/worlds/tr_room0%d/world.rbh' % (room)).encode("utf-8")+b'\x00'
        assets.append(stage)
    for screen in range(50):
        asset = str('art/screens/congrat/data%d.rbh' % (screen)).encode("utf-8")+b'\x00'
        assets.append(asset)
    for world in worlds:
        for room in range(50):
            stage = str('art/worlds/%s%d/world.rbh' % (world, room)).encode("utf-8")+b'\x00'
            assets.append(stage)
    return assets
def filenameListEarlierGames():
    filenameList = generateListOfWoodyWoodpeckerAssets()
    return filenameList
def filenameListLaterGames():
    filenameList = [
                    b'Art/Fonts/Sylfaen.rbh\x00',
                    b'Art/Fonts/Sylfaen15.rbh\x00',
                    b'Art/Fonts/Sylfaen_VRAM.rbh\x00',
                    b'Art/Fonts/Sylfaen15_VRAM.rbh\x00'
                    ]
    filenameList.extend(generateListOfNewerGameAssets())
    return filenameList
