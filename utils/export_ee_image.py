import os
import geemap

def export_ee_image_list(image_list, image_name,out_folder,region,scale):
    for image in image_list:
        print("Exporting image_name..........................................")
        out_path = os.path.join(out_folder, os.path.basename(image))
        print(out_path)
        if os.path.exists(out_path):
            print(f'{os.path.join(image_name)} already exists.')
        else:
            geemap.ee_export_image(image, out_path, scale, region)
            print(f'{os.path.join(image_name)} downloaded successfully to {out_path}.')