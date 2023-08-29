import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk


def adjust_contrast(image, factor):
    # Convert image to float32 for calculations
    image = image.astype(np.float32)
    
    # Adjust contrast by multiplying each pixel by the contrast factor
    adjusted_image = image * factor
    
    # Clip pixel values to the range [0, 255]
    adjusted_image = np.clip(adjusted_image, 0, 255)
    
    # Convert image back to uint8 format
    adjusted_image = adjusted_image.astype(np.uint8)
    
    return adjusted_image

def apply_solarization(image, threshold):
    # Invert pixel values above the threshold
    solarized_image = np.where(image > threshold, 255 - image, image)
    
    return solarized_image

# Load the image
img = cv2.imread('input_image_cat.jpg')

# Define the default color balance ratios
# Adjust contrast
contrast_factor = 1.5
# Apply solarization
solarization_threshold = 128

# Define a function to update the color balance ratios
def update_ratios(contrast_factor_value, solarization_threshold_value):
    global contrast_factor, solarization_threshold
    contrast_factor = contrast_factor_value
    solarization_threshold = solarization_threshold_value

    apply_color_balance()

# Define a function to apply the color balance transform
def apply_color_balance():
    global img, contrast_factor, solarization_threshold
    img_inline = img
    img_inline = adjust_contrast(img_inline, contrast_factor)
    img_inline = apply_solarization(img_inline, solarization_threshold)
    # Show the updated image
    cv2.imshow('Color Balanced Image', img_inline)

# Create a GUI for adjusting the color balance ratios
root = tk.Tk()
root.geometry('400x300')
root.title('Color Balance')

r_scale = tk.Scale(root, from_=0.1, to=2.0, resolution=0.01, label='contrast_factor', orient=tk.HORIZONTAL, length=200, command=lambda x: update_ratios(float(x), solarization_threshold))
r_scale.set(1.0)
r_scale.pack(pady=10)

g_scale = tk.Scale(root, from_=0, to=255, label='solarization_threshold', orient=tk.HORIZONTAL, length=200, command=lambda y: update_ratios(contrast_factor, float(y)))
g_scale.set(128)
g_scale.pack(pady=10)

apply_color_balance()

root.mainloop()
