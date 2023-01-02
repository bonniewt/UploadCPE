# import os # to import test image files
import re
import cv2
import numpy as np
import pytesseract
# to work with opencv images
import pytesseract as pt
from PIL import Image  # image submodule to work with pillow image
from pytesseract import Output

# https://nanonets.com/blog/ocr-with-tesseract/

# file name
img = cv2.imread('cpe.jpg')

# detect orientation and language script
osd = pytesseract.image_to_osd(img)
angle = re.search('(?<=Rotate: )\d+', osd).group(0)
# script = re.search('(?<=Script: )\d+', osd).group(0)
print("angle: ", angle) # prints 0 if upright
# print("script: ", script)

# img = Image.open("cpe.jpg")

# adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)


# preprocessing

# get grayscale image
def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(img):
    return cv2.medianBlur(img, 5)


# thresholding
def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)


# erotion
def erode(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(img, kernel, iterations=1)


# opening = erosion followed by dilation
def opening(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(img):
    return cv2.Canny(img, 100, 200)


# skew correction
def deskew(img):
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w // 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(img, template):
    return cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)


# pre-process
gray = get_grayscale(img)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

# add boxes around text
# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)

# print dictionary to get each word detected, their
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

# print(d.keys())

# plot the boxes
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        if re.match(date_pattern, d['text'][i]):  # check for date
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)

# extract text from image
# text = pt.image_to_string(img)
# print(text)

#
#
# # https://www.youtube.com/watch?v=7XP5WiKw56Y&ab_channel=TheSineth
#
# #
# from pdf2image import convert_from_path  # convert pdf to jpeg
#
# # test_img_path = "cpe.jpg"
#
# # convert pdf to jpeg
# pdfs = r"cpe.pdf"
# pages = convert_from_path(pdfs, 350)  # DPI >= 300
#
# i = 1
# for page in pages:
#     image_name = "Page_" + str(i) + ".jpg"
#     page.save(image_name, "JPEG")
#     i = i + 1

# # extract text from image
# image = Image.open("test.jpg")
# text = pt.image_to_string(image)
# print(text)
