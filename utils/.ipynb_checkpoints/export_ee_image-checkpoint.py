import os
import geemap

def export_ee_image_list(image_list:list,ouput_name_list:list|str,
                         out_folder:str,region:str,scale:int):
    for image in image_list:
        for output_name in ouput_name_list:
            print("Exporting image_name..........................................")
            out_path = os.path.join(out_folder,output_name + '.tif')
            print(out_path)
            if os.path.exists(out_path):
                print(f'{os.path.join(out_path)} already exists.')
            else:
                geemap.ee_export_image(image, out_path, scale, region)
                print(f'{os.path.basename(image)} downloaded successfully to {out_path}.')