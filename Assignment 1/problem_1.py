import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



#
#
#NOTE:  Use PILLOW library ONLY for reading image
#       DON'T CHANGE TEMPLATE'S ALREADY WRITTEN CODE OR THEIR WILL BE PUNISHMENT
#       You can test your code on the image we sent you
#       Dont need to convert image to gray-scale, it's already grayscale
#       Convert images to numpy array before doing operations on it
#       NEVER NEVER NEVER USE BUILT-IN FUNCTIONS FOR EITHER ( MEAN FILTER, MEDIAN FILTER, CALCULATING HISTOGRAM) OR YOU'LL Get ZERO
#
#       You'll find methods defined in template, you should implement them all.
#       Feel free to add helper functions to organize your code as you want
#
#


#function: read image with options resizing to specific width and height
#Input: path: image path
#Returns: - image as numpy array
#         - image width
#         - image height
def read_image(img_path):


    return # img, width, height


#function: Calculate the Median filter based on insertion sort
#Input: image: numpy array, width: int, height: int
#Returns: - output_image:2D numpy array
#         - time consumed by this method
def median_insertion_sort(image, width, height):

    return #out_image, time_consumed


#function: Calculate the Median filter based on histogram for an image
#Input: image: numpy array, width: int, height: int
#Returns: - output_image:2D numpy array
#         - time consumed by this method
def median_histogram(image, width, height):

    return # out_image, time_consumed


#function: auxillary function for running script
#Input: void
#Returns: time consumed of each operation and the resulted images
def main():

    input_image, width, height=read_image('image_path')

    img_1, time_1= median_insertion_sort(input_image, width, height)

    img_2, time_2=median_histogram(input_image, width, height)


    return (img_1, time_1), (img_2, time_2)


res_1 , res_2 = main()

