from naoqi import *
tts = ALProxy('ALTextToSpeech', '192.168.2.21', 9559)
tts.say('Bonjour je suis nao')
