"""
Purpose: This file is used for testing the cycle gan model made
            in task 1.
Usage: 
    python test.py <model_type> <file_name>
    model_type: could either be 1 or 2
                1 - specficies the model to convert
                    a cat/dog to human. 
                2 - specifices the model to convert
                    a human to cat/dog

"""
import sys
from numpy import expand_dims
from tensorflow.keras.preprocessing.image import img_to_array, load_img, save_img
from tensorflow_addons.layers import InstanceNormalization
from tensorflow.keras.models import load_model
import tensorflow as tf
tf.get_logger().setLevel('ERROR')


def load_image(filename, size=(64,64)):
	# load image and resize
	pixels = load_img(filename, target_size=size)
	# to numpy array
	pixels = img_to_array(pixels)
	# transform to sample
	pixels = expand_dims(pixels, 0)
	# normalise scale from [0-255] to [-1,1]
	pixels = (pixels - 127.5) / 127.5
	return pixels

def model_type(choice):
    # This is to select the model
    if len(choice) > 1 and choice[1] == "1":
        return load_model('g_model_AtoB_003850.h5', {'InstanceNormalization': InstanceNormalization})
    return load_model('g_model_BtoA_003850.h5', {'InstanceNormalization': InstanceNormalization})


def image(choice):
    # This is to get the image
    filename = "test/"
    if len(choice) > 2:
        image = load_image(filename + args[2])
    else:
        image = load_image(filename + "default_cat.jpg")
    model = model_type(choice)
    image_tar = model.predict(image)
    image_tar = (image_tar + 1) / 2.0
    save_img("output/1.jpg", image_tar[0]) 



args = sys.argv 
image(args)
print("Completed!")


