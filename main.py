import os
import cv2
import numpy as np


##############################################################################
## Variables

# Directory where scanned images of survey results are stored
data_dir = "source_material\sample_filled"

# TODO: Remove later
data_file = "answer1.png"

# Resizing parameters
img_width = 500
img_height = 600

##############################################################################

# Read the image
img = cv2.imread(os.path.join(data_dir, data_file))

# If image was successfully read - report to console
# TODO: Put in loop for all images
if(img.any()):
    print("Read image: {}".format(data_file))

# Resize image to display output (later)
img = cv2.resize(img, (img_width, img_height))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show resized image and wait forever
cv2.imshow("Original_img_resized_GRAY", img_gray)
cv2.waitKey(0)
