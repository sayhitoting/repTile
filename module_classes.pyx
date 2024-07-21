
cdef class Hexagon:
    def __init__(self, vertices, curve, edges, centroid):
        self.curve = curve
        self.vertices = vertices
        self.edges = edges
        self.centroid = centroid
