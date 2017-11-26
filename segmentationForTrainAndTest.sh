#!/bin/bash

for i in `ls dataset/train_screenshot/`
do
	echo PIG NUM: $i
	
	mkdir -p "dataset/train_screenshot_segementation/$i"
	
	python3 segmentation_keras/predict.py --weights_path segmentation_keras/pretrained/dilation8_pascal_voc.npy  --input_path "dataset/train_screenshot/$i" --output_path "dataset/train_screenshot_segementation/$i"
	
done

python3 segmentation_keras/predict.py --weights_path segmentation_keras/pretrained/dilation8_pascal_voc.npy  --input_path dataset/testA_screenshot/ --output_path dataset/testA_screenshot_segementation/