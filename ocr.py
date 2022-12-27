# import os # to import test image files
import cv2 # to work with opencv images
from PIL import Image  # image submodule to work with pillow image

# https://www.youtube.com/watch?v=7XP5WiKw56Y&ab_channel=TheSineth

import pytesseract as pt
from pdf2image import convert_from_path  # convert pdf to jpeg

test_img_path = ""

# convert pdf to jpeg
pdfs = r"cpe.pdf"
pages = convert_from_path(pdfs, 350)  # DPI >= 300

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1

# extract text from image
image = Image.open("test.jpg")
text = pt.image_to_string(image)
print(text)
