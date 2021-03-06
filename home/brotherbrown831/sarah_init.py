#Huge thankyou to Kwatter, this is his original work tailored for my use. 
#This chatbot (SARAH) is intened to provide QA services, some personal assistant services and provide interface between user
#and Trashy_bot as well as home automation devices
# Created by Nolan Jan 6,  2016

from java.lang import String

######################################################################
# SARAH is an AIML based MRL powered implementation 
######################################################################
 
aimlDir = "/home/Desktop/MRL/develop/ProgramAB"
userName = "nolan"
botName = "sarah"


######################################################################
# Inmoov portions 
###################################################################### 
#starting the InMoov-service 
i01 = Runtime.createAndStart("i01", "InMoov")
headPort = "/dev/ttyACM0"

#starting the mouth
i01.startMouth()
#i01.mouthControl.setmouth(33,140)

#start the (InMoov-)head(-service) 
head = i01.startHead(headPort)

#start the ear(-service)
i01.startEar()

# all commands MUST be before startListening
#ear.startListening()


######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Speech Recognition:" + str(data)
 
######################################################################
# Create ProgramAB chat bot
######################################################################
sarah = Runtime.createAndStart("sarah", "ProgramAB")
# start the session for the chat bot
sarah.startSession(aimlDir, "nolan", "sarah")

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
# So this just means we need the web gui, it's part of the programAB 
# service now.
wksr = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")

######################################################################
# Start the REST API for MRL
webgui = Runtime.createAndStart("webgui","WebGui")

######################################################################
# create the html filter to filter the output of program ab
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service (named the same as the inmoov's)
# TODO: consider a different voice?
######################################################################
acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
for voice in voices:
    acapelaSpeech.setVoice("Ryan") 
 
######################################################################
# MRL Routing   webgui (speech recognition) -> program ab -> htmlfilter -> inmoov
######################################################################
# Add route from webspeach to ProgramAB(sarah)
wksr.addTextListener(sarah)
# Add route from Program AB to html filter
sarah.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(acapelaSpeech)
 
# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)

