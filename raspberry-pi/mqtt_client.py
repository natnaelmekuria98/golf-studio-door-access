# raspberry-pi/mqtt_client.py
import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker="your-mqtt-broker", port=1883):
        self.client = mqtt.Client()
        self.client.connect(broker, port)
        self.client.loop_start()

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def subscribe(self, topic, callback):
        def on_message(client, userdata, msg):
            callback(json.loads(msg.payload))
        self.client.subscribe(topic)
        self.client.on_message = on_message
