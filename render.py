import numpy as np

import Constants
from shade_triangle import shade_triangle

def render(verts2d, faces, vcolors, depth, shade_t):
    # Initialize image tensor with white background
    img = np.ones((Constants.M, Constants.N, 3))
    
    # vectorized computation of faces depth
    faces_depth = np.sum(depth[faces], axis=1) / 3
    
    # sort faces array in descending  order based on faces_depth
    sorted_faces = faces[np.flip(np.argsort(faces_depth))]
    
    for face in sorted_faces:
        img = shade_triangle(img, verts2d[face], vcolors[face], shade_t)

    return img