import numpy as np

from Edge import Edge
from interpolate_vectors import interpolate_vectors

def gourauds(canvas, vertices, vcolors):
  ymin = np.min(vertices[:, 1])
  ymax = np.max(vertices[:, 1])
  
  # List that contains all the trianlge's edges
  edges = [Edge(np.delete(vertices, i, axis=0), np.delete(vcolors, i, axis=0)) for i in range(3)]
  
  # Edge bucket is a structure that contains the necessary information of an edge
  # define edge bucket data type
  edge_bucket_dtype = np.dtype({
    'names': ('ymin', 'ymax', 'slope', 'intersection', 'low_color', 'high_color'),
    'formats': (int, int, np.float32, np.float32, np.ndarray, np.ndarray)
  })
  
  # create edge buckets for every edge of the triangle
  edge_buckets = np.array(
    [(edge.ymin, edge.ymax, edge.slope(), edge.x_of_ymin, edge.low_vert_color, edge.high_vert_color)
     for edge in edges], 
    dtype=edge_bucket_dtype)
  
  # Find Active Edges List for scan-line y == ymin
  ActiveEdgesList = edge_buckets[edge_buckets['ymin'] == ymin]
  
  for y in range(ymin, ymax):
    # sort Active Edges in respect to intersection
    ActiveEdgesList = ActiveEdgesList[np.argsort(ActiveEdgesList['intersection'])]
    # Exclude edges where ymax == y from AEL
    ActiveEdgesList = ActiveEdgesList[ActiveEdgesList['ymax'] != y]
    
    # Get the left and right intersections (x ccoordinate) between current scan-line and the triangle
    left_intersection = np.ceil(ActiveEdgesList[0]['intersection'])
    right_intersection = np.ceil(ActiveEdgesList[1]['intersection'])

    # Calculate the color values of the intersection points using linear interpolation
    color_left, color_right = interpolate_vectors(ActiveEdgesList['ymin'], 
                                                  ActiveEdgesList['ymax'], 
                                                  ActiveEdgesList['low_color'],
                                                  ActiveEdgesList['high_color'], y, 2)
        
    # paint the pixels between the intersection points for the current scan-line
    for x in range(int(left_intersection), int(right_intersection)):
      canvas[y, x] = interpolate_vectors(int(left_intersection),
                                    int(right_intersection),
                                    color_left,
                                    color_right, x, 1)
    
    # -- Update ActiveEdgesList (AEL) recursively --
    # update the intersection of the already existing active edges
    # so that it corresponds to the next scan-line
    ActiveEdgesList['intersection'] += (1 / ActiveEdgesList['slope'])
    
    # Add edges where ymin == y + 1 in AEL
    newEdges = edge_buckets[edge_buckets['ymin'] == y + 1]
    ActiveEdgesList = np.append(ActiveEdgesList, newEdges)
    
  return canvas