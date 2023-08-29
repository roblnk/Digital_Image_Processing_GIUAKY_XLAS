import cv2
import numpy as np


def separable_convolution(image, kernel_horizontal, kernel_vertical, padding_mode='zero'):
    # Check if the image is grayscale or color
    if len(image.shape) == 3:
        # Separate color channels
        channels = cv2.split(image)
        conv_channels = []

        # Apply convolution to each channel separately
        for channel in channels:
            conv_horizontal = cv2.filter2D(channel, -1, kernel_horizontal, borderType=cv2.BORDER_REFLECT)
            conv_result = cv2.filter2D(conv_horizontal, -1, kernel_vertical, borderType=cv2.BORDER_REFLECT)
            conv_channels.append(conv_result)

        # Merge color channels back into an image
        conv_image = cv2.merge(conv_channels)
    else:
        # Grayscale image
        conv_horizontal = cv2.filter2D(image, -1, kernel_horizontal, borderType=cv2.BORDER_REFLECT)
        conv_image = cv2.filter2D(conv_horizontal, -1, kernel_vertical, borderType=cv2.BORDER_REFLECT)

    return conv_image


def approximate_convolution(image, kernels, padding_mode='zero'):
    # Initialize the approximation image
    approx_image = np.zeros_like(image, dtype=np.float64)

    # Perform convolution for each separable kernel
    for kernel in kernels:
        kernel_horizontal = np.reshape(kernel[0], (1, -1))
        kernel_vertical = np.reshape(kernel[1], (-1, 1))

        convolved_image = separable_convolution(image, kernel_horizontal, kernel_vertical, padding_mode)
        approx_image += convolved_image

    # Normalize the approximation image
    approx_image = cv2.normalize(approx_image, None, 0, 255, cv2.NORM_MINMAX)

    return approx_image.astype(np.uint8)


# Example usage
try:
    # Load the input image
    image = cv2.imread('darkroom.jpg', cv2.IMREAD_COLOR)

    # Check if the image is loaded successfully
    if image is None:
        raise ValueError('Failed to load the image.')

    # Define the separable kernels
    kernels = [
        (np.array([1, 2, 1]), np.array([1])),
        (np.array([1]), np.array([1, 2, 1])),
    ]

    # Perform separable convolution
    convolved_image = separable_convolution(image, kernels[0][0], kernels[0][1])

    # Perform approximate convolution
    approx_image = approximate_convolution(image, kernels)

    # Display the original, convolved, and approximated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Convolved Image', convolved_image)
    cv2.imshow('Approximated Image', approx_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f'An error occurred: {str(e)}')
