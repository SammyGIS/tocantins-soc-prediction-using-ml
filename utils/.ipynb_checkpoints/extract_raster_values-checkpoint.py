import geopandas as  gpd
import ee
import os

def  get_value_to_point(point_data:gpd.GeoDataFrame, raster_list:list) -> gpd.GeoDataFrame:
    # Get the values of slope, elevation, and land use at the location of the random points
    for raster_dataset in raster_list:
        for _, point in point_data.iterrows():
            # Get the coordinates of the point
            x = point.geometry.x
            y = point.geometry.y
            
            if type(raster_dataset) == 'ee.image.Image':
                raster_dataset.toArray()
                # Get the row and column indices of the point in the rasters
                row, col = raster_dataset.index(x, y) 
                # Extract the values of slope, elevation, and land use at the location of the point
                point_value =  raster_dataset.read(1)[row, col]
            else:
                # Get the row and column indices of the point in the rasters
                row, col = raster_dataset.index(x, y)      
                # Extract the values of slope, elevation, and land use at the location of the point
                point_value =  raster_dataset.read(1)[row, col]

    return  point_value