import os
import pandas as pd
from pathlib import Path

from get_config import get_config_dict

from shutil import copy
"""
Move the selected images to another directory called `preselcted_data`
>>> The images have to be in a directory called `raw_data` which has the following structure:
    raw_data/<subject_id>/<preprocessing>/<date>/<acquisition_id>/<file_name>.nii
"""

config = get_config_dict()
raw_data_path = config['raw_data_path']


for sampling in ['down_sample', 'up_sample']:
    if config[sampling]:

        # Read the images IDs
        print(f'Loading the `final_image_ids_{sampling}d.csv` file...')
        final_images = pd.read_csv(f'final_image_ids_{sampling}d.csv')
        print('Done')

        # Move the final images to 'preselected' directory
        for folder, dirs, filenames in os.walk(raw_data_path):
            dirname = Path(folder).name
            
            if dirname.startswith('I') and (dirname in final_images['Image Data ID'].values):
                # folder is an image ID and that ID is in the final selected IDs
                
                for filename in filenames: # should exist only one but just in case
                    src_image_path = Path(os.path.join(folder, filename))
                    dst_image_path = Path(os.path.join(folder, filename).replace("raw_data", f"preselected_data/preselected_data_{sampling}d"))
                    print(f'Moving the image {dirname} from {src_image_path} to {dst_image_path}...')
                    dst_image_path.parent.mkdir(parents=True, exist_ok=True)
                    if not dst_image_path.exists():
                        copy(src_image_path, dst_image_path)
                    print('Done')


print('\nAll the selected images were moved')