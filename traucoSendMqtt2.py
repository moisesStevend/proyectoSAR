import cv2
import numpy as np
import json
import time

img=cv2.imread('trauco.png',0)
print img, img.shape


#cv2.imshow('',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#!/usr/bin/env python
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("outTopic")

def on_message(client, userdata, msg):
  print msg.payload
  if (msg.payload == "finish"):
    print("acabo!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("10.10.40.185",1883,60)
client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

data={
	'imagen': json.dumps(img.tolist())
}

while True:
	client.publish("sendTrauco", json.dumps(data));
	time.sleep(2)

client.loop_stop()
client.disconnect()
#client.loop_forever()
