import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw


# NOTE:  Use PILLOW library ONLY for reading image
#       DON'T CHANGE TEMPLATE'S ALREADY WRITTEN CODE OR THEIR WILL BE PUNISHMENT
#       You can test your code on the image we sent you
#       Dont need to convert image to gray-scale, it's already grayscale
#       Convert images to numpy array before doing operations on it
# NEVER USE BUILT-IN FUNCTIONS FOR EITHER ( MEAN FILTER, MEDIAN FILTER, CALCULATING HISTOGRAM) OR YOU'LL Get ZERO
#
#       You'll find methods defined in template, you should implement them all.
#       Feel free to add helper functions to organize your code as you want
#


# function: Read image from pc
# Input: image_path: String
# Returns: input_img: 2D numpy array gray-scale, width: int, height: int
def read_image(noisyimg):
    img = Image.open(noisyimg)
    width = int(img.size[0])
    height = int(img.size[1])
    img = img.load()
    input_img = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            input_img[i, j] = img[i, j]
    return input_img, width, height


# function: Calculate the mean filter for an image
# Input: image: numpy array, width: int, height: int
# Returns: output_image:2D numpy array
def MeanFilter(image, width, height):
    kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]
    out = np.zeros((width, height))
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            s = 0
            for k in range(len(kernel)):
                for l in range(len(kernel)):
                    x = i + k - 1
                    y = j + l - 1
                    s += image[x, y] * kernel[k][l]
            out[i, j] = s
    return out


# function: Calculate the Median filter based on histogram for an image
# Input: image: numpy array, width: int, height: int
# Returns: output_image:2D numpy array
def MedianFilterHist(image, width, height):
    # use kernel of size 3x3

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    out = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            l = []
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < height and 0 <= y < width:
                    l.append(image[x, y])
            l.sort()
            out[i, j] = l[len(l) // 2]
    return out


# function: Apply Median filter then Mean filter on input image
# Input: input_image, width, height
# Returns: Output_image:int
def MedianThenMean(input_image, width, height):
    out = MeanFilter(MedianFilterHist(input_image, width, height), width, height)
    return out


# function: Apply Mean filter then Median filter on input image
# Input: input_image, width, height
# Returns: Output_image:int
def MeanThenMedian(input_image, width, height):
    out = MedianFilterHist(MeanFilter(input_image, width, height), width, height)
    return out

# function:Subtract both images and return the difference between them
# Input: image1, image2
# Returns: difference: 2d numpy array
def CompareImages(image1, image2):
    diff = np.zeros((image1.shape[0], image1.shape[1]))
    for i in range(image1.shape[0]):
        for j in range(image1.shape[1]):
            diff[i, j] = abs(image1[i, j] - image2[i, j])
    return diff


def viewChange(input_image, width, height, fn):

    outImg = Image.new("RGB", (width, height))
    drawableOut = ImageDraw.Draw(outImg)
    image = MedianFilterHist(input_image, width, height)
    if fn == 0:
        image = MeanFilter(input_image, width, height)
    elif fn == 2:
        image = input_image
    for i in range(len(image)):
        for j in range(len(image)):
            drawableOut.point((i, j), (int(image[i, j]), int(image[i, j]), int(image[i, j])))

    outImg.save("out" + str(fn) + ".png")


def main():
    input_image, width, height = read_image('noisyimg.png')

    img1 = MedianThenMean(input_image, width, height)
    #viewChange(img1, width, height, 1)

    img2 = MeanThenMedian(input_image, width, height)
    #viewChange(img2, width, height, 0)

    difference = CompareImages(img1, img2)
    #viewChange(difference, width, height, 2)

    return img1, img2, difference


img1, img2, difference = main()
