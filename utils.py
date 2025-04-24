import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

def remove_blue_shade_and_enhance(image):
    image = image.convert("RGB")
    np_image = np.array(image)

    # Convert to grayscale using red and green channels (minimize blue influence)
    gray = 0.5 * np_image[:, :, 0] + 0.5 * np_image[:, :, 1]
    gray = gray.astype(np.uint8)
    new_image = Image.fromarray(gray)

    # Enhance contrast and sharpness
    enhancer = ImageEnhance.Contrast(new_image)
    new_image = enhancer.enhance(2.0)
    new_image = new_image.filter(ImageFilter.SHARPEN)
    return new_image