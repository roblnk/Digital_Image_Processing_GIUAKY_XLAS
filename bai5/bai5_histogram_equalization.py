import cv2
import numpy as np

def histogram_equalization(image, fraction_black=0.05, fraction_white=0.05, gamma=1.0):
    # Step 1: Convert the image to grayscale if it's not already
    if len(image.shape) == 3:
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        v_eq = cv2.equalizeHist(v)
        hsv_eq = cv2.merge([h, s, v_eq])
        equalized_image = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
    else:
        equalized_image = cv2.equalizeHist(image)

    # Step 3: Map a certain fraction of pixels to pure black and white
    total_pixels = image.shape[0] * image.shape[1]
    black_limit = int(total_pixels * fraction_black)
    white_limit = int(total_pixels * (1 - fraction_white))
    
    # Convert the equalized image to float for calculations
    equalized_image = equalized_image.astype(float)
    
    # Step 4: Limit the local gain in the transfer function
    max_value = np.max(equalized_image)
    adjusted_image = (gamma * equalized_image / max_value) * 255
    
    equalized_image = np.where(equalized_image < adjusted_image, equalized_image, adjusted_image)
    
    return equalized_image.astype('uint8')

# Load the input image
image = cv2.imread('joker_batman.jpg', cv2.IMREAD_COLOR)

# Perform histogram equalization
equalized_image = histogram_equalization(image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
