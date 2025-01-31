# Tantalus Interactive GBA tools
Tantalus Interactive (now known as Tantalus Media) made some Game Boy Advance games with actual 3D assets and filesystems in them. The goal of this repository is to document the formats and how everything works.

### Games that ran on the Tantalus engine:
- ATV Quad Power Racing (uses a different hashing algorithm, needs to be looked into)
- Cars: Mater-National Championship
- Monster Truck Madness
- The Adventures of Jimmy Neutron Boy Genius: Attack of the Twonkies
- The Flintstones: Dino to the Rescue (unreleased)
- The Polar Express
- Top Gear Rally
- Trick Star
- Woody Woodpecker in Crazy Castle 5

### File formats:
Most games only use RBH. It's a RIFF-based container format with a "PIFF" header.
![image](https://github.com/user-attachments/assets/f9c5aa2e-51f7-42c0-937b-dd3b1878d9ff)

### RBH sections
Each RBH file has many sections. The following is a list of all known ones and what they appear to do:
- The header ("PIFF" format) (holds file information as a bunch of integers)
- BODY (stores almost any type of data)
- PACK/PKDB/PKDW/PKDL (stores almost any type of compressed data)
- GLOB (stores what appears to be global variables)
- RELC (unknown, is always near GLOB)

Despite having a length value before each RBH file, it isn't actually relevant and is only used by the engine to tell where the file starts and stops in the ROM.

Each file referenced by the file table should be looked at with the following structure:

- Length
- Data
