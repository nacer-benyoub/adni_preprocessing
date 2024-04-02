from pathlib import Path
import os

def get_config_dict():
    config = {}
    config["data_path"] = Path(r'/home/nacer/ADNI_data/ADNI1_Screening_1.5T/raw_data/') 
    config["re_process"] = True
    
    resolution_mm = 2
    config["reference_atlas_location"] = Path(f'{os.environ["FSLDIR"]}/data/standard/MNI152_T1_{resolution_mm}mm_brain.nii.gz')
    config["axial_size"] = 90
    config["save_2d"] = True
    config["remove_nii"] = True
    config["subject_limit"] = 1 # limit number of subjects to preprocess (-1 to disable)
    return config
    