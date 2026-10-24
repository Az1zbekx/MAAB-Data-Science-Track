import numpy as np
import random 
from PIL import Image

def flip(img):
    flipped = np.flip(img, axis=1)
    flipped = np.flip(flipped, axis=0)
    return flipped

def noise(arr):
    randnoise = np.random.randint(0, 50, arr.shape, dtype=np.uint8)
    res = np.clip(arr + randnoise, 0, 255)
    return res

def brighten(arr, value=40):
    brightened = np.clip(arr + value, 0, 255)
    return brightened.astype(np.uint8)


img = Image.open("images/birds.jpg")

arr = np.array(img)

arr = flip(arr)
arr = noise(arr)
arr = brighten(arr)
Image.fromarray(arr).save("output_final.jpg")
