import random 
from shapely import Point
import json
import geopandas as gpd

def generate_random_points(boundary=None, num_points=None, crs=None):
    # Generate the random points within the shapefile boundary
    points = []
    while len(points) < num_points:
        # Generate a random point within the extent of the boundary
        x = random.uniform(boundary.bounds.minx, boundary.bounds.maxx)
        y = random.uniform(boundary.bounds.miny, boundary.bounds.maxy)
        point = Point(x, y)
        
        # Check if the point is within the boundary
        if point.within(boundary.geometry.values[0]):
            points.append(point)

    # Convert the list of points to a GeoDataFrame
    if crs is None:
        crs = boundary.crs
    random_points_gdf = gpd.GeoDataFrame(geometry=points, crs=crs)
    return random_points_gdf