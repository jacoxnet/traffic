import cv2
import numpy as np
import os
import sys
import tensorflow as tf

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():
    print ('read started')
    x, y = load_data('gtsrb')
    print ('read completed')
    print (f"x length is {len(x)}")
    print (f"y length is {len(y)}")



def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # initialize image list and label list
    image_list = []
    labels = []
    # create list of categories
    categories = [str(num) for num in range(NUM_CATEGORIES)]
    # iterate through each category reading in files in subdirectory
    for category in categories:
        for name in os.listdir(os.path.join(data_dir, category)):
            # read in image, resize, and append to image list
            img = cv2.imread(os.path.join(data_dir, category, name))
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            image_list.append(img)
            # also update label for that imgae
            labels.append(int(category))
    return (image_list, labels)
    

if __name__ == "__main__":
    main()







