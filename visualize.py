from PIL import Image
import mmap

def represent(path):
    ba = None
    with open(path, 'rb') as f:
            ba = bytearray(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ))
    side = math.ceil(math.sqrt(len(ba)))
    img = Image.new('RGB', (side, side), "black")
    pixels = img.load()
    for i in range(side):
            for j in range(side):
                    index = i*side+j
                    if index < len(ba):
                            pixels[i,j] = (0, 0, ba[index])
    img.show()