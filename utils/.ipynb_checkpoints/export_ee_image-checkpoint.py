import os
import geemap

def export_ee_image_list(image_list: list, output_name_list: list,
                         out_folder: str, region: str, scale: int):

    if len(image_list) != len(output_name_list):
        raise ValueError("Length of image_list and output_name_list must be the same.")
        
    for image, output_name in zip(image_list, output_name_list):
        print(f"Exporting {output_name}...")
        out_path = os.path.join(out_folder, output_name + '.tif')
        
        if os.path.exists(out_path):
            print(f'{out_path} already exists.')
        else:
            try:
                geemap.ee_export_image(image, out_path, scale, region)
                print(f'{output_name} downloaded successfully to {out_path}.')
            except Exception as e:
                print(f'Error exporting {output_name}: {str(e)}')
