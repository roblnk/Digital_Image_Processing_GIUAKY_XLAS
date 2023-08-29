import cv2
import numpy as np

def denoise_gaussian(image, kernel_size, sigma):
    denoised_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    return denoised_image

def denoise_non_local_means(image, h, h_color, patch_size, search_window):
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, h, h_color, patch_size, search_window)
    return denoised_image

# Load the input image
image = cv2.imread('helen.png')

# Denoise the image using Gaussian filter
gaussian_denoised = denoise_gaussian(image, kernel_size=7, sigma=2.0)

# Denoise the image using non-local means
non_local_means_denoised = denoise_non_local_means(image, h=20, h_color=20, patch_size=7, search_window=21)

# Display the original image


# Display the denoised images
cv2.imshow('Gaussian Denoised Image', gaussian_denoised)

cv2.imshow('Non-Local Means Denoised Image', non_local_means_denoised)
cv2.waitKey(0)

cv2.destroyAllWindows()
