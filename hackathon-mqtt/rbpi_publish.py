import paho.mqtt.client as mqtt
import urllib.parse
import time
# Define event callbacks
    
def on_connect(mosq, obj, rc, temp):
    #print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    print("" )
def on_message(mosq, obj, msg):
    print ("on_message:: this means  I got a message from brokerfor this topic")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print ("")
def on_publish(mosq, obj, mid):
    #print("mid: " + str(mid))
    print ("")
def on_subscribe(mosq, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(mosq, obj, level, string):
    print(  string)
client = mqtt.Client("sensordata")
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
# Uncomment to enable debug messages
client.on_log = on_log
# user name has to be called before connect - my notes.
client.username_pw_set("smjlshlt", "6r_8MdvcwVy5")
client.connect("m24.cloudmqtt.com",13123, 60)
client.loop_start()
index=0
while index in range(0,5):
    client.publish ( "TempSensor", "Temperature")
    time.sleep(0.5)
    index+=1
time.sleep(2)

#client.subscribe("TempSensor")

