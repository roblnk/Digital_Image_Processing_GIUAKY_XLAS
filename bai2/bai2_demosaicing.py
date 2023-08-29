import numpy as np
import cv2

def demosaic_ahd(image):
    height, width = image.shape
    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Create empty channels for Red, Green, and Blue
    red_channel = np.zeros((height, width), dtype=np.float32)
    green_channel = np.zeros((height, width), dtype=np.float32)
    blue_channel = np.zeros((height, width), dtype=np.float32)

    # Demosaicing using Adaptive Homogeneity-Directed (AHD)
    for i in range(height):
        for j in range(width):
            if i % 2 == 0 and j % 2 == 0:
                red_channel[i, j] = image[i, j]
            elif i % 2 == 0 and j % 2 != 0:
                green_channel[i, j] = image[i, j]
            elif i % 2 != 0 and j % 2 == 0:
                green_channel[i, j] = image[i, j]
            elif i % 2 != 0 and j % 2 != 0:
                blue_channel[i, j] = image[i, j]

    # Interpolate the green channel
    for i in range(height):
        for j in range(width):
            if green_channel[i, j] == 0:
                if i > 1 and i < height - 2 and j > 1 and j < width - 2:
                    neighbor_vals = [green_channel[i-1, j], green_channel[i+1, j],
                                     green_channel[i, j-1], green_channel[i, j+1]]
                    neighbor_avg = sum(neighbor_vals) / len(neighbor_vals)
                    green_channel[i, j] = neighbor_avg

    # Interpolate the red and blue channels
    for i in range(height):
        for j in range(width):
            if red_channel[i, j] == 0:
                if i > 1 and i < height - 2 and j > 1 and j < width - 2:
                    red_vals = [red_channel[i-2, j], red_channel[i+2, j],
                                red_channel[i, j-2], red_channel[i, j+2]]
                    red_avg = sum(red_vals) / len(red_vals)
                    red_channel[i, j] = red_avg
            if blue_channel[i, j] == 0:
                if i > 1 and i < height - 2 and j > 1 and j < width - 2:
                    blue_vals = [blue_channel[i-2, j], blue_channel[i+2, j],
                                 blue_channel[i, j-2], blue_channel[i, j+2]]
                    blue_avg = sum(blue_vals) / len(blue_vals)
                    blue_channel[i, j] = blue_avg

    # Normalize the channels to 8-bit unsigned integers
    red_channel = red_channel.astype(np.uint8)
    green_channel = green_channel.astype(np.uint8)
    blue_channel = blue_channel.astype(np.uint8)

    # Combine the channels to form the RGB image
    rgb_image[:, :, 0] = red_channel
    rgb_image[:, :, 1] = green_channel
    rgb_image[:, :, 2] = blue_channel

    return rgb_image

# Load the single-channel image captured using a CFA
single_channel_image = cv2.imread('input_image2.jpg', cv2.IMREAD_GRAYSCALE)

# Perform demosaicing using bilinear interpolation
demosaiced_image = demosaic_ahd(single_channel_image)


# Save the resulting RGB image
cv2.imshow('output', demosaiced_image)
cv2.imwrite('output.png', demosaiced_image)
cv2.destroyAllWindows()
