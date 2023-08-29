import cv2
import numpy as np

# Load the input image (binary image with foreground pixels as 0s and background pixels as 255s)
image = cv2.imread('hand.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    raise ValueError('Failed to load the image.')

# Invert the image (to make foreground pixels 255 and background pixels 0)
image = cv2.bitwise_not(image)

# Compute the city block distance transform
city_block_distance = cv2.distanceTransform(image, cv2.DIST_L1, 3)

# Compute the Euclidean distance transform
euclidean_distance = cv2.distanceTransform(image, cv2.DIST_L2, 3)

# Normalize the distance transforms for visualization
city_block_distance = cv2.normalize(city_block_distance, None, 0, 255, cv2.NORM_MINMAX)
euclidean_distance = cv2.normalize(euclidean_distance, None, 0, 255, cv2.NORM_MINMAX)

# Convert the distance transforms to uint8 for display
city_block_distance = city_block_distance.astype(np.uint8)
euclidean_distance = euclidean_distance.astype(np.uint8)

# Display the distance transformed images
cv2.imshow('Orriginal Image', image)
cv2.imshow('City Block Distance Transform', city_block_distance)
cv2.imshow('Euclidean Distance Transform', euclidean_distance)
cv2.waitKey(0)
cv2.destroyAllWindows()
