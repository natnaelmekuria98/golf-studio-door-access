// server/app.js
const express = require("express");
const mqttHandler = require("./mqttHandler");
const accessValidator = require("./accessValidator");
const notifications = require("./notifications");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

// Start MQTT listener
mqttHandler.start();

// API endpoint for manual access log retrieval
app.get("/logs", (req, res) => {
  // Fetch logs from the database
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
