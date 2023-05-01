import numpy as np

import Constants
from flats import flats
from gourauds import gourauds

def render(verts2d, faces, vcolors, depth, shade_t):
    # Initialize image tensor with white background
    img = np.ones((Constants.M, Constants.N, 3))
    
    # vectorized computation of faces depth
    faces_depth = np.sum(depth[faces], axis=1) / 3
    
    # sort faces array in descending  order based on faces_depth
    sorted_faces = faces[np.flip(np.argsort(faces_depth))]
    
    # choose shader and paint the triangles
    if shade_t == 'flat':
        for face in sorted_faces:
            img = flats(img, verts2d[face], vcolors[face])
    else :
        for face in sorted_faces:
            img = gourauds(img, verts2d[face], vcolors[face])        

    return img