# CONTENTS
1. FILES AND EXPLAINATION
2. USAGE 

---------------------------------------------------------------------------------------------

## 1. FILES AND EXPLAINATION

.
├── task-1                          : This contains a cycleGAN model
    ├─ ─output                      : These are the outputs from the model
        ├── 1.jpg                   : An example of 1 output      
    ├── test                        : These would contain test images            
        ├── default_cat.jpg         : An example of a test image  
        ├── default_dog.jpg         : An example of a test image
    ├── g_model_AtoB_003850.h5      : The model which transfer from dogs/cats to humans
    ├── g_model_BtoA_003850.h5      : The model which transfer from humans to cats/dogs
    ├── humantocatsndogs.npz        : dataset file
    ├── model.ipynb                 : A python notebook contain the cycleGAN model including training 
    ├── test.py                     : This is used to test files
    └──README.md                   : Further instructions for task-1
├── task-2                          : This contains the model to classify birds
    ├── test                        : This are the test images
        ├── 3.jpg                   : An example of a test image
        ├── 4.jpg                   : An example of a test image
    ├── h5-model-2.h5               : The convolutional model
    ├── test.ipynb                  : python notebook which contains information to test all items
    ├── test.py                     : The file is used to test the model with a single image specified
    ├── train.ipynb                 : This specifies the way in which the model was trained
    └──README.md                   : Further instructions for task-2
├── task-3                          : This contains the language model to predict the text 
    ├── h5-model-3.h5               : The model
    ├── poirotInvestigates.txt      : The data being used to train the model
    ├── test.ipynb                  : The test data 
    ├── train.ipynb                 : The training notebook
    └──README.md                   : Further instructions for task-1
├── LICENSE
└── requirements.txt                : list of libaries needed.

.
├── build                   # Compiled files (alternatively `dist`)
├── docs                    # Documentation files (alternatively `doc`)
├── src                     # Source files (alternatively `lib` or `app`)
├── test                    # Automated tests (alternatively `spec` or `tests`)
├── tools                   # Tools and utilities
├── LICENSE
└── README.md

---------------------------------------------------------------------------------------------

## USAGE

(1) step 1 (optional)
    To begin you can optionally create a virtual enviroment by following these instructions

    > python -m venv env
    > source env/bin/activate

(2) step 2 
    To allow all the files to run, download the requirements
    
    > pip install -r requirements.txt

within the individual task for each model there is further instructions on how to run the files.



