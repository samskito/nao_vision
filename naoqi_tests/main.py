# -*- coding: utf-8 -*-

##Imports
from naoqi import *
import time
import Image


def showImageNao():
    camProxy = ALProxy('ALVideoDevice', '192.168.2.21', 9559)
    resolution = 2
    colorSpace = 11

    videoClient = camProxy.subscribe('python_client', resolution, colorSpace, 5)

    t0 = time.time()

    #Get Image
    naoImage = camProxy.getImageRemote(videoClient)
    t1 = time.time()

    #time for transfert
    diff = t1 - t0
    print(('Acquisition delay' + str(diff)))

    camProxy.unsubscribe(videoClient)

    #Show
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]

    im = Image.fromstring('RGB', (imageWidth, imageHeight), array)
    im.show()

##Main
flag = True
i = 0

while flag is True:
    i = i + 1
    showImageNao()
    if i > 3:
        flag = False
    time.sleep(1)