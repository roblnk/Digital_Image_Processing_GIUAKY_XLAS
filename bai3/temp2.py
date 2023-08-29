import cv2

def detect_edges(image, threshold1=100, threshold2=200):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1, threshold2)

    return edges

# Load the input image
input_image = cv2.imread('foreground.jpg')

# Detect edges using Canny edge detection
edges_image = detect_edges(input_image)

# Display the input and edges images
cv2.imshow('Input Image', input_image)
cv2.imshow('Edges Image', edges_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
