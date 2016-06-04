#! /usr/bin/python

from SimpleCV import Image, Camera
cam = Camera()
img = cam.getImage()
img.save("lunar1.jpg")

