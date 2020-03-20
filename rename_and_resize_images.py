#!/usr/local/bin/python3
# rename_and_resize_images.py
# 
# Python code to read images from a folder,
# resize them to have height and width less
# than or equal to max_pixels, and rename
# the images to the name of the folder with
# an index.
#
# input:
#   foldername -> name of folder containing images
# ouput:
#   None
#
# Questions: Talk to Elliot
#

# built in modules
import os
import argparse

# Libs
from PIL import Image

# parameters
image_extensions = ('.jpg','.jpeg','.png','.tif','.tiff','.gif')
max_pixels = 2048


def main(foldername):
    new_images = []
    new_names = []

    i = 1
    foldername_only = os.path.split(foldername)[1]
    filenames = os.listdir(foldername)
    filenames.sort()

    for filename in filenames:
        extension = os.path.splitext(filename)[1].lower()
        if extension in image_extensions:
            dst = os.path.join(foldername,f'{foldername_only}_{i}{extension}')
            src = os.path.join(foldername,filename)

            i += 1

            # Open the image, resize if necessary, save under new name
            # with Image.open(src) as im:
            im = Image.open(src)
            # Size of the image in pixels (size of original image)
            width, height = im.size

            if width > max_pixels or height > max_pixels:
                newHeight = -1
                newWidth = -1
                if width >= height:
                    newHeight = int(max_pixels/width * height)
                    newWidth = max_pixels
                else:
                    newHeight = max_pixels
                    newWidth = int(max_pixels/height * width)

                newSize = (newWidth, newHeight)
                im = im.resize( newSize, resample=Image.LANCZOS )
            
            # Store the new image (or old if not changed)
            new_images.append(im)
            new_names.append(dst)
            
            # Delete the old image
            os.remove(src)
    
    # Now save the new images
    for index, image in enumerate(new_images):
        image.save(new_names[index])
        image.close()

# Driver Code
if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('foldername')

    args = parser.parse_args()

    # Calling main() function
    main(args.foldername)
