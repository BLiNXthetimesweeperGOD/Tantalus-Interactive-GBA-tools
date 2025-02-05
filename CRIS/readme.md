# CRIS data formats

### Textures
- Colors are stored as a BGR555 palette, stored in the SpriteTemplate.rbh file
- Textures are always 8 bits per pixel and are generally stored with the model, separately from the palette

### Models
- There isn't any defined normals (the geometry is already facing the right way as-is)
- Vertices are little endian signed 16-Bit integers (X, Y, Z, 0000) (0000 is padding)
- Faces can be either tris or quads, which is determined by a single bit getting set (0x24 = tri, 0x2C = quad)
- UVs and weights are in a custom, still not fully understood format

### Animations
- Every animation starts with a bone offset list of sorts
- The data isn't fully understood, but there's X, Y and Z location/rotation/scale values for every bone. The values are little endian 16-Bit integers.
