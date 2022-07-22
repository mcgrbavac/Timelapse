#!/usr/bin/python3

import webbrowser
import pyscreenshot
from time import sleep
from datetime import datetime

#Set the snapshot interval
x_sec = 1
x_min = x_sec * 60
x_hour = x_min * 60
x_day = x_hour * 24
#Set the number of photos you want to take
y_maxPhotos = 100

counter = 0
while True:
	counter = counter + 1
	if counter < y_maxPhotos:
		#Open the webbrowser, got to URL that will take a snapshot of the stream
		strURL = "https://www.google.com"
		webbrowser.open(strURL)

		#Capture image of the snapshot taken at the URL
		pic = pyscreenshot.grab(bbox=(430, 300, 1490, 890))
		#pic.show()
		strSave = datetime.today().strftime("%Y%m%d-%H:%M:%s-")
		pic.save(strSave + ".png")
		sleep(x_day)
	else:
		exit()
