import numpy as np

class Edge:
  def __init__(self, verts2d):
    self.point_a = verts2d[0, :]
    self.point_b = verts2d[1, :]
    self.ymin = min(verts2d[:, 1])
    
  def is_horizontal(self):
    return self.point_a[1] == self.point_b[1]
    
  def is_vertical(self):
    return self.point_a[0] == self.point_b[0]
  
  def slope(self):
    if self.is_horizontal(): return 0
    
    if self.is_vertical(): return float('inf')
    
    return (self.point_a[1] - self.point_b[1]) / (self.point_a[0] - self.point_b[0])