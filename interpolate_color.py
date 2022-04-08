import numpy as np

def interpolate_color(x1, x2, x, Color1, Color2):
    t = (x2 - x) / (x2 - x1)
    return t * Color1 + (1 - t) * Color2