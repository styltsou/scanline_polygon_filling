import numpy as np

from Edge import Edge

def shade_triangle(img, verts2d, vcolors, shade_t):
    Y = img

    # find y min and y max of current triangle
    ymin = np.min(verts2d[:, 1])
    ymax = np.max(verts2d[:, 1])
    
    # List that contains all the triangles edges
    edges = [Edge(np.delete(verts2d, i, axis=0)) for i in range (3)]

    # Find ActiveEdgesList for scan line y == ymin
    ActiveEdgesList = list(filter(lambda edge: edge.ymin == ymin, edges))
    # Find ActivePoinstList for scan line y == ymin
    ActivePointsList = np.empty((1, 2), dtype='float32')

    for y in range(ymin, ymax + 1):
        # do sort AEL in respect to x

        # Init number of intersections between current scan line and triangle edges
        cross_count = 0

        # start scaning line y

        # end scaning line y

        # update AEL recursively
        # update APL recursively

    # Do stuff here
    return Y
