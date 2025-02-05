import struct
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import zlib

class fileTools:
    """
    A class to handle various operations involving files
    """
    def ext(filepath):
        """
        Returns the extension from the input filename
        """
        return os.path.splitext(filepath)[1][1:]
    def name(path):
        """
        Returns the input filename without a path
        """
        return os.path.basename(path)
    def nameNoExt(path):
        """
        Returns the filename with no extension
        """
        return os.path.splitext(os.path.basename(path))[0]
    def size(path):
        """
        Returns the size of the file referenced by the path
        """
        return os.path.getsize(path)
    def folder(path):
        """
        Returns the folder with no file attached
        """
        return os.path.dirname(path)
    def compress(data):
        """
        Compresses data (loaded as bytes) with ZLIB
        """
        return zlib.compress(data)
    def decompress(data):
        """
        Decompresses ZLIB-compressed data
        """
        return zlib.decompress(data)
    def scanForBytes(path, string):
        """
        Reads an entire file into memory and checks it for a byte string
        
        Returns: True or False, string offset if found
        Format: scanForBytes(file path, byte string)
        """
        with open(path, 'rb') as file:
            content = file.read()
            offset = content.find(string)
            return string in content, offset
    def scanForBytesUpTo(path, string, end):
        """
        Reads part of a file (from the beginning) into memory and checks
        it for a byte string.
        
        Returns: True or False, string offset if found
        Format: scanForBytesUpTo(file path, byte string, read length)
        """
        with open(path, 'rb') as file:
            content = file.read(end)
            offset = content.find(string)
            return string in content, offset
    def scanForBytesInRange(path, string, start, end):
        """
        Reads part of a file (from the specified start offset to the specified end offset)
        into memory and checks it for a byte string.
        
        Returns: True or False, string offset if found
        Format: scanForBytesInRange(file path, byte string, start offset, end offset)
        """
        with open(path, 'rb') as file:
            file.seek(start)
            content = file.read(end-start)
            offset = content.find(string)
            return string in content, offset
    def getZeroTerminatedString(file, offset):
        """
        Gets any zero-terminated string at any given offset
        """
        string = ""
        scan = b''
        with open(file, "rb") as fileWithString:
            fileWithString.seek(offset)
            while scan != b'\x00':
                scan = fileWithString.read(1)
                if scan != b'\x00':
                    string = string+scan.decode("UTF-8")
        return string
    
class dialogs:
    """
    You can quickly open a dialog with this class
    """
    def file():
        """
        Opens a file dialog and returns a single file path after you select it
        """
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfilename()
        root.destroy()
        return file
    
    def files():
        """
        Opens a file dialog and returns a list of file paths after you select them
        """
        root = tk.Tk()
        root.withdraw()
        files = filedialog.askopenfilenames()
        root.destroy()
        return files
    
    def folder():
        """
        Opens a file dialog and returns the path after you select a folder
        """
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory()
        root.destroy()
        return folder
    
    def listedFolder():
        """
        Opens a file dialog and returns the path contents after you select a folder
        """
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory()
        root.destroy()
        return os.listdir(folder)
    
    def yesno(windowName, message):
        """Creates a yes or no prompt for the user to interact with

           format: yesno(windowName, message)
        """
        root = tk.Tk()
        root.withdraw()
        result = messagebox.askyesno(windowName, message)
        if result:
            return True
        else:
            return False

class encode:
    """
    Has functions for encoding strings
    """
    def utf8(data):
        return data.encode("UTF-8")
    
    def utf16(data):
        return data.encode("UTF-16")
    
    def utf32(data):
        return data.encode("UTF-32")
    
    def ascii(data):
        return data.encode("ASCII")

class decode:
    """
    Has functions for decoding strings
    """
    def utf8(data):
        return data.decode("UTF-8")
    
    def utf16(data):
        return data.decode("UTF-16")
    
    def utf32(data):
        return data.decode("UTF-32")
    
    def ascii(data):
        return data.decode("ASCII")

class pack:
    """
    Has functions for packing a single value
    """
    def byte(value):
        return struct.pack("<b", value)
    
    def ubyte(value):
        return struct.pack("<B", value)
    
    def short(value):
        return struct.pack("<h", value)
    
    def ushort(value):
        return struct.pack("<H", value)
    
    def int(value):
        return struct.pack("<i", value)
    
    def uint(value):
        return struct.pack("<I", value)
    
    def long(value):
        return struct.pack("<q", value)
    
    def ulong(value):
        return struct.pack("<Q", value)
    
    def float(value):
        return struct.pack("<f", value)
    
    def double(value):
        return struct.pack("<d", value)

class multipack:
    """
    Has functions for packing multiple values at once
    """
    def byte(values):
        return struct.pack("<{}b".format(len(values)), *values)
    
    def ubyte(values):
        return struct.pack("<{}B".format(len(values)), *values)
    
    def short(values):
        return struct.pack("<{}h".format(len(values)), *values)
    
    def ushort(values):
        return struct.pack("<{}H".format(len(values)), *values)
    
    def int(values):
        return struct.pack("<{}i".format(len(values)), *values)
    
    def uint(values):
        return struct.pack("<{}I".format(len(values)), *values)
    
    def long(values):
        return struct.pack("<{}q".format(len(values)), *values)
    
    def ulong(values):
        return struct.pack("<{}Q".format(len(values)), *values)
    
    def float(values):
        return struct.pack("<{}f".format(len(values)), *values)
    
    def double(values):
        return struct.pack("<{}d".format(len(values)), *values)

class unpack:
    """
    Has functions for unpacking a single value
    """
    def byte(data):
        return struct.unpack("<b", data)[0]
    
    def ubyte(data):
        return struct.unpack("<B", data)[0]

    def short(data):
        return struct.unpack("<h", data)[0]
    
    def ushort(data):
        return struct.unpack("<H", data)[0]
    
    def int(data):
        return struct.unpack("<i", data)[0]
    
    def uint(data):
        return struct.unpack("<I", data)[0]

    def long(data):
        return struct.unpack("<q", data)[0]
    
    def ulong(data):
        return struct.unpack("<Q", data)[0]
    
    def float(data):
        return struct.unpack("<f", data)[0]
    
    def double(data):
        return struct.unpack("<d", data)[0]

class multiunpack:
    """
    Has functions for unpacking multiple values at once
    """
    def byte(data):
        count = len(data)
        return struct.unpack("<{}b".format(count), data)
    
    def ubyte(data):
        count = len(data)
        return struct.unpack("<{}B".format(count), data)

    def short(data):
        count = len(data) // 2
        return struct.unpack("<{}h".format(count), data)
    
    def ushort(data):
        count = len(data) // 2
        return struct.unpack("<{}H".format(count), data)
    
    def int(data):
        count = len(data) // 4
        return struct.unpack("<{}i".format(count), data)
    
    def uint(data):
        count = len(data) // 4
        return struct.unpack("<{}I".format(count), data)

    def long(data):
        count = len(data) // 8
        return struct.unpack("<{}q".format(count), data)
    
    def ulong(data):
        count = len(data) // 8
        return struct.unpack("<{}Q".format(count), data)
    
    def float(data):
        count = len(data) // 4
        return struct.unpack("<{}f".format(count), data)
    
    def double(data):
        count = len(data) // 8
        return struct.unpack("<{}d".format(count), data)

class magic:
    def checkHeader(path, magicBytes):
        """
        Checks a file's header for "magic bytes" to see if they match the input byte string
        """
        length = len(magicBytes)
        with open(path, "rb") as file:
            magic = file.read(length)
            if magic == magicBytes:
                return True
            else:
                return False
    def checkOffset(path, magicBytes, offset):
        """
        Checks a file for "magic bytes" at a specified offset to see if they match the input byte string
        """
        length = len(magicBytes)
        with open(path, "rb") as file:
            magic = file.read(length)
            if magic == magicBytes:
                return True
            else:
                return False

class BitReader:
    def __init__(self, file, offset=0):
        """Initialize BitReader with a file object opened in binary mode ('rb')
        Args:
            file: File object opened in binary mode
            offset (int): Starting byte offset in the file
        """
        self.file = file
        self.bitBuffer = 0
        self.bitsInBuffer = 0
        if offset > 0:
            self.file.seek(offset)
    
    def read(self, num_bits):
        """Read specified number of bits from the file
        
        Args:
            num_bits (int): Number of bits to read
            
        Returns:
            int: Value read from the bits
        """
        while self.bitsInBuffer < num_bits:
            byte = self.file.read(1)
            if not byte:
                raise EOFError("Reached end of file while reading bits")
            self.bitBuffer = (self.bitBuffer << 8) | int.from_bytes(byte, 'big')
            self.bitsInBuffer += 8
            
        value = (self.bitBuffer >> (self.bitsInBuffer - num_bits)) & ((1 << num_bits) - 1)
        self.bitsInBuffer -= num_bits
        return value
    
    def align(self):
        """Align the bit reader to the next byte boundary by discarding remaining bits"""
        self.bitBuffer = 0
        self.bitsInBuffer = 0
    
    def seek(self, offset):
        """Seek to a specific byte offset in the file
        
        Args:
            offset (int): Byte offset to seek to
        """
        self.file.seek(offset)
        self.bitBuffer = 0
        self.bitsInBuffer = 0
    
    def tell(self):
        """Get current position in the file
        
        Returns:
            tuple: (byte_offset, bits_into_byte)
            - byte_offset is the offset of the last byte read
            - bits_into_byte is how many bits we've read into the current byte
        """
        byte_pos = self.file.tell()
        
        if self.bitsInBuffer > 0:
            complete_bytes = self.bitsInBuffer // 8
            byte_pos -= complete_bytes
            bits_into_byte = 8 - (self.bitsInBuffer % 8)
            if bits_into_byte == 8:
                bits_into_byte = 0
        else:
            bits_into_byte = 0
            
        return (byte_pos, bits_into_byte)

class imageData:
    def maxValueForBits(bits): #Used later on in the color functions
        maxValue = (1 << bits) - 1
        return maxValue
    def indexed(bits, file, offset, order, x, y):
        """Reads indexed pixel data of the specified bit width from a file
        
           Format: indexed(bits, file, offset, order, x, y)
           bits defines how many bits there is per pixel
           file defines the file path
           offset defines the start offset in the file
           order defines the pixel order (0 is linear, 1 is reverse order)
           x is the width, y is the height
           
           Returns: A list of integers used to assign colors from a palette to each pixel
        """
        #These might be common mistakes. Fix them automatically for the user.
        if x == 0:
            x = 1
        if y == 0: 
            y = 1
        
        convertedPixels = []
        with open(file, "rb") as pixels:
            pixels.seek(offset)
            pixelReader = BitReader(pixels)
            for vertical in range(y):
                for horizontal in range(x):
                    if order == 0:  #Linear order (1, 2)
                        pixel1 = pixelReader.read(bits)
                        pixel2 = pixelReader.read(bits)
                        convertedPixels.extend([pixel1, pixel2])
                    elif order == 1:#Reverse order (2, 1)
                        pixel2 = pixelReader.read(bits)
                        pixel1 = pixelReader.read(bits)
                        convertedPixels.extend([pixel1, pixel2])
        return convertedPixels
    def indexedFrame(bits, file, offset, order, x, y, frame):
        """Reads indexed pixel data of the specified bit width from a file (and gets the specified frame)
        
           Format: indexed(bits, file, offset, order, x, y)
           bits defines how many bits there is per pixel
           file defines the file path
           offset defines the start offset in the file
           order defines the pixel order (0 is linear, 1 is reverse order)
           x is the width, y is the height
           frame is the frame number you want parsed
           
           Returns: A list of integers used to assign colors from a palette to each pixel
        """
        #These might be common mistakes. Fix them automatically for the user.
        if x == 0:
            x = 1
        if y == 0: 
            y = 1
        
        convertedPixels = []
        with open(file, "rb") as pixels:
            pixels.seek(offset)
            pixelReader = BitReader(pixels)
            for frames in range(frame): #Skip forward (frame) number of frames
                for vertical in range(y):
                    for horizontal in range(x):
                        pixelReader.read(bits)
                        pixelReader.read(bits)
            for vertical in range(y):
                for horizontal in range(x):
                    if order == 0:  #Linear order (1, 2)
                        pixel1 = pixelReader.read(bits)
                        pixel2 = pixelReader.read(bits)
                        convertedPixels.extend([pixel1, pixel2])
                    elif order == 1:#Reverse order (2, 1)
                        pixel2 = pixelReader.read(bits)
                        pixel1 = pixelReader.read(bits)
                        convertedPixels.extend([pixel1, pixel2])
        return convertedPixels
    def bgr555(file, offset, alphaMode, x, y):
        """Reads a BGR555/5551 palette from a file at the specified offset
        
           Format: bgr555(file, offset, alphaMode)
           file defines the file path
           offset defines the start offset in the file
           alphaMode defines if there is or isn't an alpha channel - 1 for True, 0 for False
           x is the width, y is the height
           
           Returns: A list of integers used to assign colors from a palette
           For color palettes, X should be the color count and Y should be 1
        """
        #These might be common mistakes. Fix them automatically for the user.
        if x == 0:
            x = 1
        if y == 0: 
            y = 1
        if alphaMode > 1:
            alphaMode = 1
        
        convertedPixels = []
        with open(file, "rb") as pixels:
            pixels.seek(offset)
            pixelReader = BitReader(pixels)
            for vertical in range(y):
                for horizontal in range(x):
                    blue = pixelReader.read(5)
                    green = pixelReader.read(5)
                    red = pixelReader.read(5)
                    alpha = pixelReader.read(1)
                    
                    blue = (blue * 255) // 31
                    green = (green * 255) // 31
                    red = (red * 255) // 31
                    alpha = alpha * 255
                    
                    if alphaMode == 0:
                        convertedPixels.append((red, green, blue))
                    elif alphaMode == 1:
                        convertedPixels.append((red, green, blue, alpha))
        return convertedPixels
    def rgb555(file, offset, alphaMode, x, y):
        """Reads an RGB555/5551 palette from a file at the specified offset
        
           Format: rgb555(file, offset, alphaMode)
           file defines the file path
           offset defines the start offset in the file
           alphaMode defines if there is or isn't an alpha channel - 1 for True, 0 for False
           x is the width, y is the height
           
           Returns: A list of integers used to assign colors from a palette
           For color palettes, X should be the color count and Y should be 1
        """
        #These might be common mistakes. Fix them automatically for the user.
        if x == 0:
            x = 1
        if y == 0: 
            y = 1
        if alphaMode > 1:
            alphaMode = 1
        
        convertedPixels = []
        with open(file, "rb") as pixels:
            pixels.seek(offset)
            pixelReader = BitReader(pixels)
            for vertical in range(y):
                for horizontal in range(x):
                    red = pixelReader.read(5)
                    green = pixelReader.read(5)
                    blue = pixelReader.read(5)
                    alpha = pixelReader.read(1)
                    
                    red = (red * 255) // 31
                    green = (green * 255) // 31
                    blue = (blue * 255) // 31
                    alpha = alpha * 255
                    
                    if alphaMode == 0:
                        convertedPixels.append((red, green, blue))
                    elif alphaMode == 1:
                        convertedPixels.append((red, green, blue, alpha))
        return convertedPixels

    def bgrCustomWidths(file, offset, alphaMode, x, y, redBits, blueBits, greenBits, alphaBits):
        """Reads a BGR palette from a file at the specified offset with the specified bit widths
        
           Format: bgr555(file, offset, alphaMode, x, y, redBits, blueBits, greenBits)
           file defines the file path
           offset defines the start offset in the file
           alphaMode defines if there is or isn't an alpha channel - 1 for True, 0 for False
           x is the width, y is the height
           The bit values determine the bit width of each value
           
           Returns: A list of integers used to assign colors from a palette
           For color palettes, X should be the color count and Y should be 1
        """
        #These might be common mistakes. Fix them automatically for the user.
        if x == 0:
            x = 1
        if y == 0: 
            y = 1
        if alphaMode > 1:
            alphaMode = 1
        
        convertedPixels = []
        with open(file, "rb") as pixels:
            pixels.seek(offset)
            pixelReader = BitReader(pixels)
            for vertical in range(y):
                for horizontal in range(x):
                    blue = pixelReader.read(blueBits)
                    green = pixelReader.read(greenBits)
                    red = pixelReader.read(redBits)
                    if alphaBits > 0:
                        alpha = pixelReader.read(alphaBits)
                    
                    blue = (blue * 255) // imageData.maxValueForBits(blueBits)
                    green = (green * 255) // imageData.maxValueForBits(greenBits)
                    red = (red * 255) // imageData.maxValueForBits(redBits)
                    if alphaBits > 0:
                        alpha = (alpha * 255) // imageData.maxValueForBits(alphaBits)
                    
                    if alphaMode == 0:
                        convertedPixels.append((red, green, blue))
                    elif alphaMode == 1:
                        convertedPixels.append((red, green, blue, alpha))
        return convertedPixels
    def rgbCustomWidths(file, offset, alphaMode, x, y, redBits, blueBits, greenBits, alphaBits):
        """Reads an RGB palette from a file at the specified offset with the specified bit widths
        
           Format: rgbCustomWidths(file, offset, alphaMode, x, y, redBits, blueBits, greenBits)
           file defines the file path
           offset defines the start offset in the file
           alphaMode defines if there is or isn't an alpha channel - 1 for True, 0 for False
           x is the width, y is the height
           The bit values determine the bit width of each value
           
           Returns: A list of integers used to assign colors from a palette
           For color palettes, X should be the color count and Y should be 1
        """
        #These might be common mistakes. Fix them automatically for the user.
        if x == 0:
            x = 1
        if y == 0: 
            y = 1
        if alphaMode > 1:
            alphaMode = 1
        
        convertedPixels = []
        with open(file, "rb") as pixels:
            pixels.seek(offset)
            pixelReader = BitReader(pixels)
            for vertical in range(y):
                for horizontal in range(x):
                    red = pixelReader.read(redBits)
                    green = pixelReader.read(blueBits)
                    blue = pixelReader.read(greenBits)
                    if alphaBits > 0:
                        alpha = pixelReader.read(alphaBits)
                    
                    red = (red * 255) // imageData.maxValueForBits(redBits)
                    green = (green * 255) // imageData.maxValueForBits(greenBits)
                    blue = (blue * 255) // imageData.maxValueForBits(blueBits)
                    if alphaBits > 0:
                        alpha = (alpha * 255) // imageData.maxValueForBits(alphaBits)
                    
                    if alphaMode == 0:
                        convertedPixels.append((red, green, blue))
                    elif alphaMode == 1:
                        convertedPixels.append((red, green, blue, alpha))
        return convertedPixels
    def readBgr555Palette(file, offset, numColors): #For cases where the palette is little endian
        palette = []
        with open(file, "rb") as f:
            f.seek(offset)
            for i in range(numColors):
                bgr555 = struct.unpack('<H', f.read(2))[0]
                b = (bgr555 & 0x1F) << 3
                g = ((bgr555 >> 5) & 0x1F) << 3
                r = ((bgr555 >> 10) & 0x1F) << 3
                palette.append((r, g, b))
        return palette
    
    #TO-DO: Implement a color sorting function so people can define a custom color order for palettes
    #Palette decoders should be designed to be reused to decode non-indexed (RGB/BGR/RGBA/BGRA) image data.

class offset:
    def RAMOffsetToBinaryOffset(RAMOffset, ROMBaseOffset):
        """Takes an offset (from a pointer table) and subtracts the ROM base offset from it
           to get the true offset in the binary file.
           Used for reversing binaries compiled for cartridge-based systems"""
        return RAMOffset-ROMBaseOffset
    def relativeOffsetToOffset(relativeOffset, baseOffset):
        """Takes an offset (from a pointer table) and adds it to a base offset for the true offset in a file
           Used for reversing a ton of formats
           (LeapPad ROMs being an example of this) and files embedded within other files"""
        return relativeOffset+baseOffset
    def wordToInt(wordAlignedOffset):
        """Takes a word-aligned offset and multiplies it by 2.
           Used for reversing VTech V.Smile games."""
        return wordAlignedOffset*2
    def intToWord(intAlignedOffset):
        """Takes a 32-Bit Integer-aligned offset and integer divides it by 2.
           Used for reversing VTech V.Smile games."""
        return intAlignedOffset//2
