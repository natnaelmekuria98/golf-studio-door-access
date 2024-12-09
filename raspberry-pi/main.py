# raspberry-pi/main.py
from mqtt_client import MqttClient
from keypad_input import Keypad
from door_control import DoorControl

mqtt_client = MqttClient()
keypad = Keypad()
door = DoorControl()

def on_validation_response(message):
    response = message['valid']
    if response:
        print("Access granted!")
        door.open()
    else:
        print("Access denied!")

mqtt_client.subscribe("golfstudio/access/pi-id/response", on_validation_response)

while True:
    code = keypad.read_code()
    mqtt_client.publish("golfstudio/access/pi-id/validate", code)
