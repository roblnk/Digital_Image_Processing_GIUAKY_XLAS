import cv2
import numpy as np


def apply_unsharp_mask(image, sigma=1.0, strength=1.0):
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)
    sharpened = cv2.addWeighted(image, 1 + strength, blurred, -strength, 0)
    return sharpened


def apply_bilateral_filter(image, d=9, sigma_color=75, sigma_space=75):
    filtered = cv2.bilateralFilter(image, d, sigma_color, sigma_space)
    return filtered


# Example usage
try:
    # Load the input image
    image = cv2.imread('darkroom.jpg', cv2.IMREAD_COLOR)

    # Check if the image is loaded successfully
    if image is None:
        raise ValueError('Failed to load the image.')

    # Apply unsharp mask sharpening
    sharpened_image = apply_unsharp_mask(image, sigma=2.0, strength=1.5)

    # Apply bilateral filter for blurring and noise removal
    filtered_image = apply_bilateral_filter(image, d=9, sigma_color=75, sigma_space=75)

    # Display the original, sharpened, and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.imshow('Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f'An error occurred: {str(e)}')
