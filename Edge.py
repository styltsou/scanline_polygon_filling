import numpy as np

class Edge:
  def __init__(self, verts2d, vcolors):
    self.point_a = verts2d[0, :]
    self.point_b = verts2d[1, :]
    self.ymin = min(verts2d[:, 1])
    self.ymax = max(verts2d[:, 1])
    self.x_of_ymin = verts2d[np.argmin(verts2d[:, 1]), 0]
    # Color of edge's lower vertex
    self.low_vert_color = vcolors[np.argmin(verts2d[:, 1])]
    # Color of edge's higher vertex
    self.high_vert_color = vcolors[np.argmax(verts2d[:, 1])]
    
  # returns True if the edge is vertical
  def is_vertical(self):
    return self.point_a[0] == self.point_b[0]
  
  def slope(self):
    if self.is_vertical(): return float('inf')
    
    return (self.point_a[1] - self.point_b[1]) / (self.point_a[0] - self.point_b[0])