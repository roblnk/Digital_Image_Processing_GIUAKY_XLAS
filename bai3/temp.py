import cv2
import numpy as np

# Load the foreground and background images
foreground = cv2.imread('bai3\\foreground_image.jpg')
background = cv2.imread('bai3\\background_image.jpg')
# Resize the foreground to match the size of the background
background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

# Convert the foreground and background images to float
foreground = foreground.astype(float)
background = background.astype(float)

# Calculate the difference between the foreground and background images
diff = cv2.absdiff(foreground, background)

# Convert the difference image to grayscale
gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale difference image to get a binary mask
ret, mask = cv2.threshold(gray_diff, 50, 255, cv2.THRESH_BINARY)

# Apply the mask to the foreground image
foreground_masked = cv2.bitwise_and(foreground, foreground, mask=mask)

# Invert the mask to get the background
mask_inv = cv2.bitwise_not(mask)
background_masked = cv2.bitwise_and(background, background, mask=mask_inv)

# Combine the foreground and background
result = cv2.add(foreground_masked, background_masked)

# Save the result image
cv2.imwrite('result.jpg', result)
