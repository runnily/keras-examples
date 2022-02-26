# Bird Classification [30 %]
This corresponds to the task 2 for the coursework. 

## CONTENTS:
1. USAGE
2. FUTHER DETAILS

## 1. USAGE

The images in the test folder contain input images to the model.

To test the model run command:

> python test.py <file_name>

file_name: is the name of the file within test

The output would be the type of bird species on command prompt

EXAMPLE:
> python test.py 3.jpg

Here we are specifying "3.jpg" the input image. The output should appear on command prompt
providing the type of bird species.

To test your own images add your image within "test/"

## 2. FUTHER DETAILS

The train.ipynb includes information of the process of training the model. 
You can run/look at this notebook to reproduce the same results. 

**HOWEVER** before running train.ipynb please download the required dataset from:
(1) http://homepages.cs.ncl.ac.uk/stephen.mcgough/Teaching/birds.zip

Unzip file and rename folder to "bird". 
Please ensure that this folder is within this current directory

The test.ipynb is for testing the whole dataset from the downloaded bird folder. You can 
run/look at this notebook to reproduce the same results.

For details on the other files, refer to "assignment/README.txt" 
