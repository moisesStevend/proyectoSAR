#!/usr/bin/env python
import numpy as np
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("diapos")

def on_message(client, userdata, msg):
  print msg.payload
  #if (msg.payload == "finish"):
  #  print("acabo!")
  #  client.disconnect()
    
client = mqtt.Client(transport='websockets')
#client.connect("test.mosquitto.org",8080,60)
client.connect("10.10.40.185",9001,60)

client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

data={
	'data': json.dumps(np.array([[1,2],[3,4]]).tolist())
}


while True:
	men = raw_input('ingrese: ')
	#if men=='envio':
	client.publish("sar", json.dumps(data));
	#elif men=='salir':
	#	client.publish("display1", 'finish');
	#	break

client.loop_stop()
client.disconnect()
#client.loop_forever()
