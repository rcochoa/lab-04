import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("rcochoa/ping")
    client.message_callback_add("rcochoa/ping",on_message_ping)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_ping(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())
    client.publish("rcochoa/pong", f"{int(msg.payload)+1}")
    time.sleep(1)

if __name__ == '__main__':

    num = 0

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect

    client.connect(host="172.20.10.3", port=1883, keepalive=60)

    time.sleep(1)
    
    client.loop_forever()