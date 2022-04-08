import numpy as np

from Edge import Edge
from interpolate_color import interpolate_color

def shade_triangle(img, verts2d, vcolors, shade_t):
  ymin = np.min(verts2d[:, 1])
  ymax = np.max(verts2d[:, 1])
  
  # List that contains all the trianlge's edges
  edges = [Edge(np.delete(verts2d, i, axis=0), np.delete(vcolors, i, axis=0)) for i in range(3)]
  
  # Edge bucket is a structure that contains information about an edge
  # define edge bucket data type
  edge_bucket_dtype = np.dtype({
    'names': ('ymin, ymax', 'slope', 'intersection'),
    'formats': (int, int, np.float, int)
  })
  
  # Find Active edges list for scan line y == ymin
  ActiveEdgesList = np.array(
    [(edge.ymin, edge.ymax, edge.slope(), edge.x_of_ymin) for edge in edges if not edge.is_horizontal()],
    dtype=edge_bucket_dtype)
  
  for y in range(ymin, ymax):
    # sort Active Edges in respect to intersection
    ActiveEdgesList = ActiveEdgesList[np.argsort(ActiveEdgesList['intersection'])]
    
    for i in range(ActiveEdgesList.shape[0]):
      # do a for loop here
      if shade_t == 'flat':
        for x in range(1):
          # paint pixel using the center mass of vetrices colors
          img[y, x] = np.sum(vcolors, axis=1) / 3 
      elif shade_t == 'gouraud':
        # Add a comment here
        color_left = interpolate_color()
        color_right = interpolate_color()
        
        for x in range(1):
          img[x, y] = interpolate_color(0, 0, x, color_left, color_right)
    
    # do some ActiveEdgesList updates here
    
    # return img 
    return img