import sys
import numpy as np
from PIL import Image
import time 

def load_img(path):
    try:
        return np.array(Image.open(path).convert('RGB'))
    except FileNotFoundError:
        print(f"Chyba: Soubor {path} nebyl nalezen.")
        sys.exit(1)

def find_diff(pxo, px1, px2):
    diff1 = np.array_equal(pxo, px1)
    diff2 = np.array_equal(pxo, px2) 
    diffs = np.array_equal(px1, px2)

    if diff1 and diff2:
        return " "
    elif diff1:
        return "2"
    elif diff2:
        return "1"
    elif diffs:
        return "1"
    else:
        return "E"

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

height, width, channels = img1.shape

maps = []


new_img = np.zeros((height, width, 3), dtype=np.uint8)

for x in range(height):
    maps.append([])
    for y in range(width):
        pxo = imgO[x, y]
        px1 = img1[x, y]
        px2 = img2[x, y]

        pxdiff = find_diff(pxo, px1, px2)
        maps[x].append(pxdiff)
        if pxdiff == " ":
            new_img[x, y] = pxo
        elif pxdiff == "1":
            new_img[x, y] = px1
        elif pxdiff == "2":
            new_img[x, y] = px2
        else:
            new_img[x, y] = [255, 0, 0]
            print(f"find mearge error at {x}, {y}")

output_img = Image.fromarray(new_img)
output_img.save('output.png')



