import geopandas as  gpd
import os

def  get_value_to_point(point_data:gpd.GeoDataFrame, raster_list:list) -> gpd.GeoDataFrame:
    # Get the values of slope, elevation, and land use at the location of the random points
    for raster_dataset in raster_list:
        for index, point in point_data.iterrows():
            # Get the coordinates of the point
            x = point.geometry.x
            y = point.geometry.y
            
            # Get the row and column indices of the point in the rasters
            row, col = raster_dataset.index(x, y)
            
            # Extract the values of slope, elevation, and land use at the location of the point
            point_value =  raster_dataset.read(1)[row, col]
        
            # Append the values to the point's attributes
            point_data.loc[index,os.path.basename(point_data)] = point_value
            
        # read the dataset to view the addeded columns
    return point_data