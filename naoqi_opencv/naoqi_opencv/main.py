# -*- coding: utf-8 -*-
# Geoffroy Baumier - 02/17/2016
# Open a window with nao's camera stream using opencv
# Open Cv doc: http://bit.ly/1KVOxMA

# Imports
from vision_definitions import *
from cv2 import *
from numpy import *
from naoqi import *

# Variables
videoProxy = ALProxy('ALVideoDevice', '192.168.2.21', 9559)
whichCamera = 0  # 0 top, 1 bottom
stopKey = 0

# Register a generic video module to the video input module
videoModule = videoProxy.subscribeCamera("OpenCVCamera",
whichCamera, kVGA, kBGRColorSpace, 30)

while(stopKey != 1048603):
    # Get an image
    naoImage = videoProxy.getImageRemote(videoModule)

    # Image container is an array as follow: http://bit.ly/1Tq90fa
    width = naoImage[0]
    height = naoImage[1]
    numberLayers = naoImage[2]
    imageArray = naoImage[6]

    # Create a new 1-D array initialized from raw binary or text data in a
    # string and gives a new shape to this array without changing its data.
    rgbImage = fromstring(imageArray,
    dtype="uint8").reshape(height, width, numberLayers)

    # Show the image
    imshow("Nao Stream", rgbImage)

    # Get keyboard: waiting on 'esc'
    stopKey = waitKey(1)

# Cleanup
destroyAllWindows()
videoProxy.unsubscribe(videoModule)