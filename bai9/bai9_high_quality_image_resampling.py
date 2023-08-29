import cv2
import numpy as np
from scipy import signal

def resample_image(image, scaling_factor, filter_type='windowed_sinc'):
    # Calculate the new dimensions based on the scaling factor
    new_width = int(image.shape[1] * scaling_factor)
    new_height = int(image.shape[0] * scaling_factor)

    # Create the filter kernel based on the selected filter type
    if filter_type == 'nearest':
        kernel = np.ones((1, 1))
    elif filter_type == 'bilinear':
        kernel = np.array([[0.25, 0.5, 0.25]])
    elif filter_type == 'windowed_sinc':
        cutoff_freq = 0.5 / scaling_factor
        kernel = signal.firwin(15, cutoff_freq, window='hamming')

    # Resize the image using the selected filter
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Apply the filter kernel along each axis
    if filter_type != 'nearest':
        resized_image = cv2.filter2D(resized_image, -1, kernel)
    
    return resized_image

# Load the input image
image = cv2.imread('chantroi.jpg')

# Define the scaling factor for resampling
scaling_factor = 2  # Increase image size by a factor of 2

# Define the filter types to use for resampling
filter_types = ['nearest', 'bilinear', 'windowed_sinc']

# Perform resampling using different filters
resampled_images = []

for filter_type in filter_types:
    resampled_image = resample_image(image, scaling_factor, filter_type)
    resampled_images.append(resampled_image)

# Concatenate the resampled images horizontally
result_image = np.hstack(resampled_images)

# Display the result
cv2.imshow('Original Image', image)
cv2.imshow('Resampling Comparison', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
