// server/mqttHandler.js
const mqtt = require("mqtt");
const accessValidator = require("./accessValidator");
const notifications = require("./notifications");

const client = mqtt.connect(process.env.MQTT_BROKER_URL);

client.on("connect", () => {
  client.subscribe("golfstudio/access/+/validate");
});

client.on("message", async (topic, message) => {
  const code = message.toString();
  const deviceId = topic.split("/")[2]; // Extract Raspberry Pi ID
  const isValid = await accessValidator.validateCode(code);

  // Publish response
  client.publish(
    `golfstudio/access/${deviceId}/response`,
    JSON.stringify({ valid: isValid })
  );

  if (isValid) {
    notifications.sendSuccessNotification(deviceId);
  } else {
    notifications.sendAlert(deviceId, code);
  }
});
