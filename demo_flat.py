import numpy as np
import cv2

from render import render

if __name__ == "__main__":
    data = np.load('hw1.npy', allow_pickle=True)
    dict = data.tolist()
    
    # extract arrays from dictionary
    verts2d = dict['verts2d'].astype(int)
    faces = dict['faces']
    vcolors = dict['vcolors']
    depth = dict['depth']

    img = render(verts2d, faces, vcolors, depth, 'flat')
    
    # convert img colors from range [0,1] to range [0,255] before saving
    cv2.imwrite('flat_shading.png', img * 255)
