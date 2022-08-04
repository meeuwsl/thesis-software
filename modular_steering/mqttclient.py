import paho.mqtt.client as mqtt



#constants
MQTT_ADDRESS = '192.168.1.104'
MQTT_TOPIC = 'test/message'


class MqttClient():
    

    def __init__(self, address_broker, on_message):
        self.address_broker = address_broker
        self.on_message = on_message

        print("new broker with address broker: " + self.address_broker)
    
        self.client = mqtt.Client("ABS")
        
    def start(self, topics):
        self.client.connect(MQTT_ADDRESS)
        
        for t in topics:
            print(t)
            self.client.subscribe(t)
            #self.client.message_callback_add()

        self.client.on_message = self.callback
        
        self.client.loop_start()
        print("mqtt client started")



    def callback(self, client, userdata, message):
        #self.on_message(message)
        print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

    def send(self, topic, message):
        self.client.publish(topic, payload=message, qos=0, retain=False)
        print("called send")



