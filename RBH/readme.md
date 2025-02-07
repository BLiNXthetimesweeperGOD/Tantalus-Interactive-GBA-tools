# This is a work in progress!
Do not expect this to be 100% accurate yet.

# RBH file format info
RBH files are RIFF-based containers which can be broken up into chunks:

- The header (lists out data sizes for each chunk)
- PACK/PK(DB/DW/DL)/BODY sections which contain data
- RELC/GLOB sections which contain various variables


### PIFF Chunk/Header Formats
In the RBH format, the first chunk is formatted like this:

```
50 49 46 46 ("PIFF")
(32-Bit Data Length)
52 42 48 46 ("RBHF"/RBH Format)
```

For the header ("RBHH"/RBH Header) chunk, it's formatted like this:
```
52 42 48 48 ("RBHH"/RBH Header)
(32-Bit Data Length)
(Data)

Data format:
(32-bit unknown value)
Section length
16-Bit (unknown)
16-Bit (unknown)
(repeat until data end, this should at least give you the section count)
```

### GLOB format
GLOB stores variables (offsets, maybe?). The formatting is known, but what exactly it does still needs work.

```
47 4C 4F 42 ("GLOB")
(32-Bit Data Length)
(Data)

Data format:
(32-Bit count, 32-Bit unknown)
(32-Bit value, 32-Bit value)
(Repeat value part {count}-1 times)
```
