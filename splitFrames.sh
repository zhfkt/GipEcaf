#!/bin/bash

if (( $# < 1 ))
then
	echo "splitFrames.sh [folder]";
	exit 0;
	
else 

	folder=$1
	
fi


for i in `ls $folder`; 
do 
	echo ${i}; 
	j=`cut -d '.' -f 1 <<< $i`; 
	mkdir -p screenshot/${j}/; 
#	ffmpeg -i ${folder}/${i} -vf fps=1 screenshot/${j}/${j}_%d.jpg ; 
	ffmpeg -i ${folder}/${i}  screenshot/${j}/${j}_%d.jpg ; 
done
