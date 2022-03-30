import numpy as np
from interpolate_color import interpolate_color

def shade_flat(vcolors):
  return np.sum(vcolors, axis=1) / 3

def shade_gouraud(edges, active_points, vcolors, x, y):
  # for active point_a color find its edge
  active_point_a = 0
  edge_a = 0
  color_a = interpolate_color()
  
  # for active_point_b color find its edge
  active_point_b = 0
  edge_b = 0
  color_b = interpolate_color()
  
  
  return interpolate_color(active_point_a, active_point_b, np.array([x, y]), color_a, color_b)