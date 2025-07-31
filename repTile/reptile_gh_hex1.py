"""Grasshopper Script"""
import Grasshopper
import ghpythonlib.components as gh

class Tile:
    def __init__(self, vertices, vectors, polyline, centroid):
        self.vertices = vertices
        self.vectors = vectors
        self.polyline = polyline
        self.centroid = centroid

    def Tiling (self, num_layers):
        return None


def CreateHexagon(points):
    if not points or len(points) != 4:
        ghenv.Component.AddRuntimeMessage(
            Grasshopper.Kernel.GH_RuntimeMessageLevel.Error,
            "Expected 4 points, got {}".format(len(points) if points else 0)
        )
        return None
    
    # create edge vectors from points
    list_vectors = []
    user_vectors = []
    for i in range(len(points)):
        if i < len(points) - 1:
            vector = gh.Vector2Pt(points[i], points[i+1], False).vector
            user_vectors.append(vector)
            list_vectors.append(vector)
    
    for vector in user_vectors: # complete edge vectors from tiling rules
        list_vectors.append(vector)


    # complete shape via tiling rules
    point_4 = gh.Move(points[-1], -list_vectors[0]).geometry
    point_5 = gh.Move(point_4, -list_vectors[1]).geometry
    list_points = points
    list_points.append(point_4)
    list_points.append(point_5)

    # create tile shape
    polyline = gh.PolyLine(list_points,True)

    # find centroid
    centroid = gh.Area(polyline).centroid

    HexagonTile = Tile(list_points, list_vectors, polyline, centroid)

    return HexagonTile


# Call function
repTile = CreateHexagon(points)
polyline = repTile.polyline
