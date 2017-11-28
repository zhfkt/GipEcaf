#!/bin/bash

for i in `ls dataset/train_screenshot/`
do
	echo PIG NUM: $i
	
	mkdir -p "dataset/train_screenshot_segementation/$i"
	
	cd fcnSegmentation
	
	python3 fcnChainer.py -m pretrained/fcn8s_from_caffe.npz --img-files ../dataset/train_screenshot/$i/*  -o ../dataset/train_screenshot_segementation/$i/ 
	
	cd ..
	
done
