# CRIS data formats

### Textures
- Colors are stored as a BGR555 palette, stored in the SpriteTemplate.rbh file
- Textures are always 8 bits per pixel and are generally stored with the model, separately from the palette
- Textures aren't tiled

### Models
- There isn't any defined normals (the geometry is already facing the right way as-is)
- Vertices are little endian signed 16-Bit integers (X, Y, Z, 0000) (0000 is padding)
- Faces can be either tris or quads, which is determined by a single bit getting set (0x24 = tri, 0x2C = quad)
- UVs are corner-based

Formatting examples:

Quad:
```
00 00                                                   (16-Bit, every entry starts with this)
{Something weight related?}                             (8-Bit)
{set as tri or quad byte}                               (8-Bit)
{vertex index 1, 2, 3 and 4}                            (8 Bits per entry)
{4 Corner UVs, ordered the same as the vertex indices}  (16 Bits per entry)
```

Tri:
```
00 00                                                   (16-Bit, every entry starts with this)
{Something weight related?}                             (8-Bit)
{set as tri or quad byte}                               (8-Bit)
{vertex index 1, 2, 3 and 4 (4 is always 0)}            (8 Bits per entry)
?? ?? ?? ?? ?? ??                                       (unknown)
{3 Corner UVs, ordered the same as the vertex indices}  (16 Bits per entry)
```

Examples of entries taken directly from a model's data (each line is an entry):

```
Quads:
00 00 48 2C C7 C8 C4 C3 1F 69 22 68 22 57 1C 57 
00 00 56 2C C6 C9 CA C2 2C 58 2C 68 34 68 34 57 
00 00 80 2C C6 C5 CB C9 2C 58 27 58 29 68 2C 68 
00 00 48 2C CA C7 C3 C2 34 68 37 69 39 57 34 57 
00 00 5C 2C C8 CB C5 C4 22 68 29 68 27 58 22 57 
00 00 80 2C 71 C9 CB 70 0D 6D 0E 67 06 66 04 6B 

Tris:
00 00 48 24 C7 CA 73 00 BB 00 FF FF FF FF 37 69 34 68 34 6A 
00 00 54 24 C9 73 CA 00 FF FF BE 00 B9 00 2C 68 34 6A 34 68 
00 00 54 24 74 CB C8 00 FF FF BC 00 FF FF 22 6A 29 68 22 68 
00 00 48 24 C8 C7 74 00 B8 00 FF FF C0 00 22 68 1F 69 22 6A
```

### Animations
- Every animation starts with a bone offset list of sorts
- The data isn't fully understood, but there's X, Y and Z location/rotation/scale values for every bone. The values are little endian 16-Bit integers.
