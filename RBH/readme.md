# This is a work in progress!
Do not expect this to be 100% accurate yet.

# RBH file format info
RBH files are RIFF-based containers which can be broken up into chunks:

- The header (lists out data sizes for each chunk)
- PACK/PK/BODY sections which contain data
- RELC/GLOB sections which contain various variables


### Header
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
