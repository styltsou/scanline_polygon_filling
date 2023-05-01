import numpy as np
import cv2
from matplotlib import pyplot as plt

from render import render

if __name__ == "__main__":
    data = np.load('h1.npy', allow_pickle=True)
    dict = data.tolist()
    
    # extract arrays from dictionary
    verts2d = dict['verts2d'].astype(int)
    faces = dict['faces']
    vcolors = dict['vcolors']
    depth = dict['depth']

    img = render(verts2d, faces, vcolors, depth, 'flat')
    
    # convert image from BGR to RGB format
    img = cv2.cvtColor(img.astype('float32'), cv2.COLOR_BGR2RGB)
    
    # convert img colors from range [0,1] to range [0,255] before saving
    cv2.imwrite('flat_shading.png', img * 255)
