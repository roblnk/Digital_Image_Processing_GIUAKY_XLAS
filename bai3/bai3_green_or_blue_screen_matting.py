import cv2
import numpy as np

def blue_screen_matting(foreground, background):
    # Resize the foreground and background images to the desired size
    target_size = (background.shape[1], background.shape[0])
    foreground = cv2.resize(foreground, target_size)
    background = cv2.resize(background, target_size)

    # Convert the foreground and background images to the HSV color space
    foreground_hsv = cv2.cvtColor(foreground, cv2.COLOR_BGR2HSV)
    background_hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)

    # Define the blue color range for matting
    lower_blue = np.array([90, 50, 50])  # Adjust these values as needed
    upper_blue = np.array([130, 255, 255])  # Adjust these values as needed

    # Create a mask of the blue color region in the foreground image
    mask = cv2.inRange(foreground_hsv, lower_blue, upper_blue)

    # Invert the mask to select the non-blue region in the foreground image
    inverted_mask = cv2.bitwise_not(mask)

    # Use the mask to extract the blue region from the foreground image
    foreground_blue = cv2.bitwise_and(foreground, foreground, mask=inverted_mask)

    # Use the mask to extract the non-blue region from the background image
    background_non_blue = cv2.bitwise_and(background, background, mask=mask)

    # Combine the blue region from the foreground image and the non-blue region from the background image
    result = cv2.add(foreground_blue, background_non_blue)

    return result

def green_screen_matting(foreground, background):
    # Convert the foreground and background images to the HSV color space
    foreground_hsv = cv2.cvtColor(foreground, cv2.COLOR_BGR2HSV)
    background_hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)

    # Define the green color range for matting
    lower_green = np.array([40, 50, 50])  # Adjust these values as needed
    upper_green = np.array([80, 255, 255])  # Adjust these values as needed

    # Create a mask of the green color region in the foreground image
    mask = cv2.inRange(foreground_hsv, lower_green, upper_green)

    # Invert the mask to select the non-green region in the foreground image
    inverted_mask = cv2.bitwise_not(mask)

    # Use the mask to extract the green region from the foreground image
    foreground_green = cv2.bitwise_and(foreground, foreground, mask=inverted_mask)

    # Use the mask to extract the non-green region from the background image
    background_non_green = cv2.bitwise_and(background, background, mask=mask)

    # Combine the green region from the foreground image and the non-green region from the background image
    result = cv2.add(foreground_green, background_non_green)

    return result




# Load the foreground and background images
foreground = cv2.imread('foreground.jpg')
background = cv2.imread('background_image.jpg')

# Specify the desired width and height for resizing
target_width = 800
target_height = 500

# Resize the foreground and background images
foreground = cv2.resize(foreground, (target_width, target_height))
background = cv2.resize(background, (target_width, target_height))




# Perform blue screen matting
result = green_screen_matting(foreground, background)

# Display the original foreground, background, and matted image
cv2.imshow('Foreground', foreground)
cv2.imshow('Background', background)
cv2.imshow('Matted Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
