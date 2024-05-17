import geopandas as gpd
import ee

def get_value_to_point(point_data: gpd.GeoDataFrame, raster_list: list) -> gpd.GeoDataFrame:
    # Iterate over each raster dataset
    for raster_dataset in raster_list:
        # Check if the raster dataset is an Earth Engine image
        if isinstance(raster_dataset, ee.image.Image):
            # Get the pixel values for each point using Earth Engine
            values = raster_dataset.reduceRegions(collection=point_data, reducer=ee.Reducer.first(), scale=30)
            # Merge the extracted values with the point data
            point_data = point_data.merge(values, left_index=True, right_index=True)
        else:
            # Get the pixel values for each point using Rasterio
            raster_values = []
            for _, point in point_data.iterrows():
                x = point.geometry.x
                y = point.geometry.y
                row, col = raster_dataset.index(x, y)
                point_value = raster_dataset.read(1)[row, col]
                # Add the raster value to the list
                raster_values.append(point_value)
            # Add the raster values as a new column to the GeoDataFrame
            point_data[raster_dataset.name] = raster_values
    
    return point_data

