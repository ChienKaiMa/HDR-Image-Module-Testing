####################################################################################
# 2020/12/08
# Author: Chien-Kai Ma
# Test HDR functionality of https://github.com/vivianhylee/high-dynamic-range-image
# To make the code work, it is suggested to modify line 236 and 246 in hdr.py.
# Add "dst=None" to the parameters of cv2.normalize.
####################################################################################
import hdr
import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join
import time
from math import *

mypath = "example"
# 484x324, png
imgSet0 = [join(mypath, f) for f in listdir(mypath) if isfile(
    join(mypath, f)) and 'sample' in f and not 'sample2' in f]
images0 = []
for image in imgSet0:
    image = cv2.imread(image)
    images0.append(image)

# 1087x723, jpg
imgSet1 = [join(mypath, f) for f in listdir(mypath)
           if isfile(join(mypath, f)) and 'sample2' in f]
images1 = []
for image in imgSet1:
    image = cv2.imread(image)
    images1.append(image)

# The exposure times are not provided in the examples
# I use the numbers in my phone to test.
log_exposure_times0 = [log(1/1000), log(1/500),
                       log(1/250), log(1/125), log(1/64), log(1/32)]
log_exposure_times1 = [log(1/1000), log(1/500), log(1/250),
                       log(1/125), log(1/64), log(1/32), log(1/16)]

# About 15 seconds
start = time.time()
hdr_result0 = hdr.computeHDR(images0, log_exposure_times0)
cv2.imwrite('result0.png', hdr_result0)
end = time.time()
print(round(end - start, 2), 's')

# About 100 seconds
start = time.time()
hdr_result1 = hdr.computeHDR(images1, log_exposure_times1)
cv2.imwrite('result1.png', hdr_result1)
end = time.time()
print(round(end - start, 2), 's')
