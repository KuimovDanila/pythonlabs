import numpy as np
from PIL import Image

img_array = np.array(Image.open("C:/Users/LEGION/Downloads/lunar_images/lunar_images/lunar03_raw.jpg").convert('L'))

min_val, max_val = np.min(img_array), np.max(img_array)
enhanced_array = ((img_array - min_val) / (max_val - min_val) * 255).astype(np.uint8)

Image.fromarray(enhanced_array).save("C:/Users/LEGION/Downloads/lunar03.jpg")
