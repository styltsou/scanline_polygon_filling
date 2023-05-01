import numpy as np

def interpolate_vectors(p1, p2, V1, V2, xy, dim):
    t = (p2 - xy) / (p2 - p1)
    return t * V1 + (1 - t) * V2