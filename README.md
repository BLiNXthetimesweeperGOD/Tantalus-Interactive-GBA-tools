# Tantalus Interactive GBA tools
Tantalus Interactive (now known as Tantalus Media) made some Game Boy Advance games with actual 3D assets and filesystems in them. The goal of this repository is to document the formats and how everything works.

### Games that ran on the Tantalus engine:
- ATV Quad Power Racing
- Cars: Mater-National Championship
- Monster Truck Madness
- The Adventures of Jimmy Neutron Boy Genius: Attack of the Twonkies
- The Flintstones: Dino to the Rescue (unreleased)
- The Polar Express
- Top Gear Rally
- Trick Star
- Woody Woodpecker in Crazy Castle 5 (uses a different algorithm, needs to be looked into)

### File formats:
Most games only use RBH. It's a RIFF-based container format with a "PIFF" header.
![image](https://github.com/user-attachments/assets/f9c5aa2e-51f7-42c0-937b-dd3b1878d9ff)

### RBH sections
Each RBH file has many sections. The following is a list of all known ones and what they appear to do:
- The header ("PIFF" magic, "RBHF" format)
- The RBHH section (header)
- BODY (stores almost any type of data)
- PACK/PKDB/PKDW/PKDL (stores almost any type of compressed data) (you can decompress it with [this](https://github.com/leeao/RORPSPTOOL))
- GLOB (stores what appears to be global variables)
- RELC (unknown, is always near GLOB)

Despite having a length value before each RBH file, it isn't actually relevant and is only used by the engine to tell where the file ends in the ROM.

Each file referenced by the file table should be looked at with the following structure:

- Length
- Data

# To-Do
- Figure out how filenames are handled in earlier versions of the engine
- Go through all games with "%s" strings and manually add all filenames that they'd reference to a big list
- Fully document the sections of the RBH format
- Finish documenting CRIS
- Make a GUI for the decompression tool (but still respect the original developer by not outright stealing it/throwing it in here)
- Move all documentation into a "documentation" folder, the main page should exclusively be for explaining what this is for
