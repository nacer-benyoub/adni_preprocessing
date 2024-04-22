#!/bin/bash

cd /home/nacer/adni_preprocessing

echo "Running Step 1: Image Preselection..."
jupyter nbconvert --to notebook --execute image_preselection.ipynb --inplace
echo "Step 1 completed successfully"

echo "Running Step 2: Moving Selected Images..."
python move_selected_images.py > move_selected_images.txt
echo "Step 2 completed successfully"

echo "Running Step 3: Preprocessing..."
python main.py > main.txt
echo "Step 3 completed successfully"

echo "Running Step 4: Moving Preprocessed Images..."
jupyter nbconvert --to notebook --execute label_preprocessed_data.ipynb --inplace
echo "Step 4 completed successfully"