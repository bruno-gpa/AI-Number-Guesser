from PIL import Image
import numpy as np


def get_pixels(cou):
    img = Image.open("Model/pintura.png")
    pixels = img.load()
    mat = []

    for i in range(img.size[0]):
        row = []
        for j in range(img.size[1]):
            row.append(255 - (pixels[j, i]))
        mat.append(row)

    if cou % 2 == 0:
        print("\n>>> MAPA DE PIXELS\n")
        for x in mat:
            print(x)

    return np.array(mat)/255
