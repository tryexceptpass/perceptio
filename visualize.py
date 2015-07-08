""" File Visualizer.

Usage:
    visualize.py <filename> [--mmap | --np-mmap | --np-memmap | --np-fullcolor]

Options:
    --np-fullcolor  Use numpy to extract data in 4-byte chunks and draw in full color
    --np-memmap     Use numpy but run it with .memmap instead of .fromfile
    --mmap          Use mmap and regular file i/o instead of numpy fromfile.
    --np-mmap       Use mmap but stick it in a numpy array and use skimage
    --version       Show version.
    -h --help       Show this screen.
"""

from PIL import Image
import mmap
import math
import numpy as np
import struct
from docopt import docopt
from skimage import io

def npfullcolor(path):
    """Show a square image that represents the speciied file using numpy.memmap"""

    data = np.memmap(path, dtype=np.uint32, mode='r')

    side = math.ceil(math.sqrt(len(data)))
    
    img = Image.new('RGB', (side, side), "black")
    pixels = img.load()

    for i in range(side):
        for j in range(side):
            index = i * side + j
            if index < len(data):
                pixels[i, j] = struct.unpack("BBBB", data[index])

    img.show()

def npmemmaprepresent(path):
    """Show a square image that represents the speciied file using numpy.memmap"""

    data = np.memmap(path, dtype=np.uint8, mode='r')

    side = math.ceil(math.sqrt(len(data)))
    
    img = Image.new('RGB', (side, side), "black")
    pixels = img.load()

    for i in range(side):
        for j in range(side):
            index = i * side + j
            if index < len(data):
                pixels[i, j] = (data[index], data[index], 0)

    img.show()

def nprepresent(path):
    """Show a square image that represents the speciied file using numpy.fromfile"""

    data = np.fromfile(path, dtype=np.uint8)

    side = math.ceil(math.sqrt(len(data)))
    
    img = Image.new('RGB', (side, side), "black")
    pixels = img.load()

    for i in range(side):
        for j in range(side):
            index = i * side + j
            if index < len(data):
                pixels[i, j] = (data[index], data[index], 0)

    img.show()


def skrepresent(path):
    """Show a square image that represents the file specified starting from an np.zeros array"""

    data = None
    with open(path, 'rb') as infile:
        data = bytearray(mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ))
    side = math.ceil(math.sqrt(len(data)))

    #img = Image.new('RGB', (side, side), "black")
    pixels = np.zeros(shape=(side, side, 3), dtype=np.uint8)

    for i in range(side):
        for j in range(side):
            index = i*side+j
            if index < len(data):
                pixels[i, j, 0] = data[index]
                pixels[i, j, 1] = data[index]
                pixels[i, j, 2] = 0
    
    io.imshow(pixels)
    io.show()

def represent(path):
    """Show a square image that represents the file specified"""

    data = None
    with open(path, 'rb') as infile:
        data = bytearray(mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ))
    side = math.ceil(math.sqrt(len(data)))
    img = Image.new('RGB', (side, side), "black")
    pixels = img.load()
    for i in range(side):
        for j in range(side):
            index = i*side+j
            if index < len(data):
                pixels[i, j] = (data[index], data[index], 0)
    img.show()

if __name__ == '__main__':
    ARGS = docopt(__doc__, version="0.1")

    if ARGS['--mmap']:
        represent(ARGS['<filename>'])
    elif ARGS['--np-mmap']:
        skrepresent(ARGS['<filename>'])
    elif ARGS['--np-memmap']:
        npmemmaprepresent(ARGS['<filename>'])
    elif ARGS['--np-fullcolor']:
        npfullcolor(ARGS['<filename>'])
    else:
        nprepresent(ARGS['<filename>'])
