import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


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


#function: Read image from pc
#Input: image_path: String
#Returns: input_img: 2D numpy array gray-scale, width: int, height: int
def read_image(img_path):

    return input_img, width, height



#function: Calculate the mean filter for an image
#Input: image: numpy array, width: int, height: int
#Returns: output_image:2D numpy array
def MeanFilter(image, width, height):
    kernel=[[1/9,1/9,1/9],
            [1/9,1/9,1/9],
            [1/9,1/9,1/9]]

    return out



#function: Calculate the Median filter based on histogram for an image
#Input: image: numpy array, width: int, height: int
#Returns: output_image:2D numpy array
def MedianFilterHist(image, width, height):
    #use kernel of size 3x3

    return out



#function: Apply Median filter then Mean filter on input image
#Input: input_image, width, height
#Returns: Output_image:int
def MedianThenMean(input_image, width, height):

    return out


#function: Apply Mean filter then Median filter on input image
#Input: input_image, width, height
#Returns: Output_image:int
def MeanThenMedian(input_image, width, height):

    return out

#function:Subtract both images and return the difference between them
#Input: image1, image2
#Returns: difference: 2d numpy array
def CompareImages(image1, image2):

    return diff


def main():

    input_image, width, height=read_image('image_path')

    img1= MedianThenMean(input_image, width, height)

    img2=MeanThenMedian(input_image, width, height)

    difference = CompareImages(img1, img2)

    return img1, img2, difference

img1, img2, difference = main()