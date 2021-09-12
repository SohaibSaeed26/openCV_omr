import os               # To navigate our file structure
import cv2              # Contour detection 
import numpy as np      # Not used yet
import my_utils         # To stack images and other helpful tools


##############################################################################
## Variables

# Directory where scanned images of survey results are stored
data_dir = "source_material\sample_filled"

# TODO: Remove later - implement going through every file in every folder
data_file = "answer1.png"

# Resizing parameters
img_width = 500
img_height = 600

# Gaussian Blur parameters
gaus_blur_kernel = (5, 5)
gaus_blur_sigmaX = 1

# Canny parameters
canny_thrs1 = 10
canny_thrs2 = 50

# My Utils parameters
stack_img_scale = 0.6

##############################################################################
## Main code

# Read the image
img = cv2.imread(os.path.join(data_dir, data_file))

# If image was successfully read - report to console
# TODO: Put in loop for all images
if(img.any()):
    print("Read image: {}".format(data_file))

# Resize every image
img = cv2.resize(img, (img_width, img_height))

# Convert to greyscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur filter to help detect edges
img_blur = cv2.GaussianBlur(img_gray, gaus_blur_kernel, gaus_blur_sigmaX)

# Detect edges
img_canny = cv2.Canny(img_blur, canny_thrs1, canny_thrs2)

# Create a stack of images all joined together
img_array = ([img, img_gray, img_blur, img_canny])
stacked_imgs = my_utils.stackImages(img_array, stack_img_scale)

# Show images and wait forever
cv2.imshow("Images", stacked_imgs)
cv2.waitKey(0)
