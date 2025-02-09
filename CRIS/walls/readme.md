# CRIS wall format documentation

### Header 

(Formatting is unknown, has 2 16-Bit values of an unknown purpose)

### Offset table
```
24-bit offset (relative to data start offset)
8-bit height value (how tall this strip of the wall is)
```

### Wall data
Wall data is 8 bits per pixel and isn't tiled
