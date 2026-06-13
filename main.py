import sys
import numpy as np
from PIL import Image

def load_img(path):
    return np.array(Image.open(path).convert('RGB'))

imgO = load_img('org.png')
img1 = load_img('diff_1.png')
img2 = load_img('diff_2.png')

shape_O = tuple(int(x) for x in imgO.shape)
shape_1 = tuple(int(x) for x in img1.shape)
shape_2 = tuple(int(x) for x in img2.shape)

if not (shape_O == shape_1 == shape_2):
    print(f"Chyba: Obrázky mají odlišné vlastnosti!")
    print(f"ORG: {shape_O}    DIFF 1: {shape_1}    DIFF 2: {shape_2}")
    sys.exit(1)

dime = img1.shape

height, width, channels = img1.shape

maps = []

for x in range(height):
    maps.append([])
    for y in range(width):
        pxo = imgO[x, y]
        px1 = img1[x, y]
        px2 = img2[x, y]
        
        diff1 = np.array_equal(pxo, px1)
        diff2 = np.array_equal(pxo, px2) 
        diffs = np.array_equal(px1, px2)

        if diff1 and diff2:
            maps[x].append(" ")
        elif diff1:
            maps[x].append("2")
        elif diff2:
            maps[x].append("1")
        elif diffs:
            maps[x].append("B")
        else:
            maps[x].append("E")

print(f"|{"-"*(width*2-1)}|")
for i in maps:
    print(f"|{" ".join(i)}|")
print(f"|{"-"*(width*2-1)}|")



