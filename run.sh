#!/bin/bash

cd /home/nacer/adni_preprocessing
jupyter nbconvert --to notebook --execute image_preselection.ipynb --inplace
python main.py > main.txt
jupyter nbconvert --to notebook --execute label_preprocessed_data.ipynb --inplace