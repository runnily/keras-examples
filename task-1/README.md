# Using an existing model [30 %]
This corresponds to the task 1 for the coursework. 

## CONTENTS:
1. USAGE
2. FUTHER DETAILS

## 1. USAGE

The images in the test folder contain input images to the model.
output folder contains the model output images from the images in test folder.

To test the model run command:

> python test.py <model_type> <file_name>

model_type: could either be 1 or 2
        1 - specifics the model to convert
            a cat/dog too human. 
        2 - specifics the model to convert
            a human to cat/dog

file_name: is the name of the file within test

The output "1.jpg" will be stored in the output folder.

EXAMPLE:
> python test.py 1 default_dog.jpg

Where we are specifying the use to model "1" along with the input image "default_dog.jpg". The
output should appear within the output folder.

You can add your own images to test for the model to translate

## 2. FUTHER DETAILS

The model.ipynb contains the code for the model. for details on the other files, refer to 
"assignment/README.txt" 
