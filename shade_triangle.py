import numpy as np

from Edge import Edge
from interpolate_color import interpolate_color

def shade_triangle(img, verts2d, vcolors, shade_t):
  Y = img
  
  ymin = np.min(verts2d[:, 1])
  ymax = np.max(verts2d[:, 1])
  
  # List that contains all the trianlge's edges
  edges = [Edge(np.delete(verts2d, i, axis=0), np.delete(vcolors, i, axis=0)) for i in range(3)]
  
  # Edge bucket is a structure that contains information about an edge
  # define edge bucket data type
  edge_bucket_dtype = np.dtype({
    'names': ('ymin', 'ymax', 'slope', 'intersection'),
    'formats': (int, int, np.float32, np.float32)
  })
  
  edge_buckets = np.array(
    [(edge.ymin, edge.ymax, edge.slope(), edge.x_of_ymin) for edge in edges], 
    dtype=edge_bucket_dtype)
  
  # Find Active edges list for scan line y == ymin
  # ActiveEdgesList = np.array(
  #   [(edge.ymin, edge.ymax, edge.slope(), edge.x_of_ymin) for edge in edges if not edge.is_horizontal() if edge.ymin == ymin],
  #   dtype=edge_bucket_dtype)
  
  ActiveEdgesList = edge_buckets[np.logical_and(edge_buckets['slope'] != 0, edge_buckets['ymin'] == ymin)]
  # ActiveEdgesList = edge_buckets[edge_buckets['ymin'] == ymin]
  # ActiveEdgesList = ActiveEdgesList[ActiveEdgesList['slope'] != 0]
  
  for y in range(ymin, ymax):
    # sort Active Edges in respect to intersection
    ActiveEdgesList = ActiveEdgesList[np.argsort(ActiveEdgesList['intersection'])]
    
    for i in range(ActiveEdgesList.shape[0] - 1):
      # do a for loop here
      if shade_t == 'flat':
        for x in range(int(ActiveEdgesList[i]['intersection']), int(ActiveEdgesList[i + 1]['intersection'])):
          # paint pixel using the center mass of vetrices colors
          Y[y, x] = np.sum(vcolors, axis=1) / 3 
      elif shade_t == 'gouraud':
        # Add a comment here
        color_left = interpolate_color()
        color_right = interpolate_color()
        
        for x in range(int(ActiveEdgesList[i]['intersection']), int(ActiveEdgesList[i + 1]['intersection'])):
          Y[x, y] = interpolate_color(0, 0, x, color_left, color_right)
    
    # Update ActiveEdgesList (AEL) recursively
    # Exclude edges where ymax == y
    ActiveEdgesList = ActiveEdgesList[ActiveEdgesList['ymax'] != y]
    
    # update intersection for pre-existing edges
    ActiveEdgesList['intersection'] = ActiveEdgesList['intersection'] + (1 / ActiveEdgesList['slope'])
    
    # Add edges where ymin == y + 1 in AEL
    newEdges = edge_buckets[edge_buckets['ymin'] == y + 1]
    ActiveEdgesList = np.append(ActiveEdgesList, newEdges)
    
  # Do I need extra code to handle horizontal edges??
  
  # return img 
  return Y