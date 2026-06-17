import sys
import numpy as np
from PIL import Image

def load_img(path):
    try:
        return np.array(Image.open(path).convert('RGB'))
    except FileNotFoundError:
        print(f"Chyba: Soubor {path} nebyl nalezen.")
        sys.exit(1)

class GitablePicture:
    def __init__(self) -> None:
        pass 

    def _validate_img(self):
        shape_O = tuple(int(x) for x in self.imgO.shape)
        shape_1 = tuple(int(x) for x in self.img1.shape)
        shape_2 = tuple(int(x) for x in self.img2.shape)

        if not (shape_O == shape_1 == shape_2):
            print(f"Chyba: Obrázky mají odlišné vlastnosti!")
            print(f"ORG: {shape_O}    DIFF 1: {shape_1}    DIFF 2: {shape_2}")
            sys.exit(1)

        self.height, self.width, self.channels = self.img1.shape

    def _get_diff(self):
        pass

    def mearge(self, org, img1, img2):
        self.imgO = load_img(org)
        self.img1 = load_img(img1)
        self.img2 = load_img(img2)

        _validate_img()

