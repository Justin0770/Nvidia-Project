#Imports
import numpy
import jetson.inference
import jetson.utils

net = jetson.inference.detectNet
camera = jetson.utils.videoSource("/dev/video0")

#Calculations
