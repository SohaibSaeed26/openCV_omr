import os
import cv2
import numpy as np


##############################################################################
## Variables

# Directory where scanned images of survey results are stored
data_dir = "C:\Sohaib\personal_projects\omr\source_material\sample_filled"

# TODO: Remove later
data_file_1 = "answer1.png"
data_file_2 = "answer2.png"
data_file_3 = "answer3.png"
data_file_4 = "answer4.png"
data_file_5 = "answer5.png"

# Resizing parameters
img_width = 500
img_height = 600

##############################################################################

# Read the image
img = cv2.imread(os.path.join(data_dir, data_file_1))

# If image was successfully read - report to console
# TODO: Put in loop for all images
if(img.any()):
    print("Read image: {}".format(data_file_1))

# Resize image to display output (later)
img = cv2.resize(img, (img_width, img_height))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show resized image and wait forever
cv2.imshow("Original_img_resized_GRAY", img_gray)
cv2.waitKey(0)