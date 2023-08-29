import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

# Load the image
img = cv2.imread('input_image_cat.jpg')

# Define the default color balance ratios
r_ratio = 1.0
g_ratio = 1.0
b_ratio = 1.0

# Define a function to update the color balance ratios
def update_ratios(r_value, g_value, b_value):
    global r_ratio, g_ratio, b_ratio
    r_ratio = r_value
    g_ratio = g_value
    b_ratio = b_value
    apply_color_balance()

# Define a function to apply the color balance transform
def apply_color_balance():
    global img, r_ratio, g_ratio, b_ratio
    img_inline = img
    # Split the image into its color channels
    b, g, r = cv2.split(img_inline)
    # Apply the color balance ratios to each channel
    b = np.uint8(np.clip(b * b_ratio, 0, 255))
    g = np.uint8(np.clip(g * g_ratio, 0, 255))
    r = np.uint8(np.clip(r * r_ratio, 0, 255))
    # Merge the channels back into an image
    img_inline = cv2.merge((b, g, r))
    # Show the updated image
    cv2.imshow('Color Balanced Image', img_inline)

# Create a GUI for adjusting the color balance ratios
root = tk.Tk()
root.geometry('400x300')
root.title('Color Balance')

r_scale = tk.Scale(root, from_=0.1, to=2.0, resolution=0.01, label='Red', orient=tk.HORIZONTAL, length=200, command=lambda x: update_ratios(float(x), g_ratio, b_ratio))
r_scale.set(1.0)
r_scale.pack(pady=10)

g_scale = tk.Scale(root, from_=0.1, to=2.0, resolution=0.01, label='Green', orient=tk.HORIZONTAL, length=200, command=lambda x: update_ratios(r_ratio, float(x), b_ratio))
g_scale.set(1.0)
g_scale.pack(pady=10)

b_scale = tk.Scale(root, from_=0.1, to=2.0, resolution=0.01, label='Blue', orient=tk.HORIZONTAL, length=200, command=lambda x: update_ratios(r_ratio, g_ratio, float(x)))
b_scale.set(1.0)
b_scale.pack(pady=10)

apply_color_balance()

root.mainloop()
