import rawpy
import imageio
import numpy as np
from skimage.restoration import denoise_tv_chambolle

# Read the raw image using rawpy
raw = rawpy.imread('input.raw')

# Demosaic using APM algorithm
rgb = raw.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=16)

# Denoise using total variation filtering
rgb_denoised = np.zeros_like(rgb)
for i in range(3):
    rgb_denoised[..., i] = denoise_tv_chambolle(rgb[..., i], weight=0.1)

# Save the output image
imageio.imwrite('output.png', rgb_denoised)
