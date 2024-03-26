from pathlib import Path
import os

def get_config_dict():
    config = {}
    config["data_path"] = Path(r"./raw_data/") 
    config["re_process"] = False
    
    resolution_mm = 2
    config["reference_atlas_location"] = Path(f'{os.environ["FSLDIR"]}/data/standard/MNI152_T1_{resolution_mm}mm_brain.nii.gz')
    config["axial_size"] = 90
    config["save_2d"] = True
    config["remove_nii"] = False
    return config
    