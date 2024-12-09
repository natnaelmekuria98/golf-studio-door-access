# golf-studio-door-access

Designing and Implementing a Secure Door Access System for a Golf Studio
1. System Overview

The system integrates the following components:

    Booking Platform: Generates six-digit access codes after booking confirmation.
    Raspberry Pi: Serves as the edge device to manage door access, validate codes, and control the door motor.
    Node.js Server: Central application server that handles MQTT communication and code validation.
    MQTT Broker: Facilitates real-time communication between the server and the Raspberry Pi.
    Database: Stores booking and access code information securely.
    Notification Service: Sends alerts and notifications for access logs and suspicious activities.

2. System Architecture

    Booking Flow:
        Customers book a slot via the booking platform.
        The booking platform generates a unique, time-bound six-digit access code.
        The code is sent to the customer via email or SMS.

    Access Flow:
        The customer enters the code on the keypad (connected to the Raspberry Pi).
        The Raspberry Pi sends the entered code via MQTT to the Node.js server for validation.
        The server validates the code and sends a response back to the Raspberry Pi.
        If valid, the Raspberry Pi triggers the door motor to unlock.

    Logging and Notification:
        Every access attempt is logged with timestamps.
        Notifications are sent for successful accesses or suspicious activities (e.g., multiple failed attempts).

3. Implementation Steps
Hardware Setup

    Raspberry Pi:
        Connect a keypad for code entry.
        Use a relay module to control the door motor.
        Install an Ethernet or Wi-Fi module for network connectivity.
    Door Motor:
        Use a motorized lock mechanism compatible with relay modules.
    MQTT Broker:
        Deploy an MQTT broker (e.g., Mosquitto) on the same network or a cloud service.

Software Development

    Node.js Server
        Dependencies:
            mqtt: For MQTT communication.
            express: For API endpoints.
            bcrypt: For encrypting access codes.
            dotenv: For environment variable management.
        Functionality:
            Validate access codes against the database.
            Publish validation results to the MQTT broker.
            Log all access attempts and suspicious activities.

    Raspberry Pi Script
        Dependencies:
            mqtt: For MQTT communication.
            gpiozero: For controlling GPIO pins (door motor).
        Functionality:
            Read input from the keypad.
            Publish entered codes to the MQTT broker.
            Subscribe to validation responses and trigger the motor if the code is valid.

    MQTT Communication
        Topic Structure:
            golfstudio/access/<raspberry_pi_id>/validate for sending codes to the server.
            golfstudio/access/<raspberry_pi_id>/response for receiving validation responses.
        Encrypted communication using TLS.

    Access Code Generation
        Generate random six-digit codes.
        Hash codes with bcrypt before storing them in the database.

    Database
        Store booking details and hashed access codes.
        Use indexed columns for quick lookup.

    Notification Service
        Integrate with a service like Twilio or AWS SES for sending notifications.
        Send real-time alerts for successful accesses or suspicious activities.

4. Security Features

    Encrypted Communication:
        Use TLS for MQTT communication.
    Code Validation:
        Validate codes server-side to prevent tampering.
    Robust Logging:
        Log every access attempt with timestamps and results.
    Rate Limiting:
        Implement rate limits to prevent brute-force attacks.
    Administrative Alerts:
        Send alerts for unusual activities (e.g., >5 failed attempts within 10 minutes).

5. Scalability Considerations

    Deploy the Node.js server on a scalable cloud platform (e.g., AWS, GCP).
    Use a distributed MQTT broker (e.g., EMQX) for handling multiple Raspberry Pis.
    Integrate the system with additional booking platforms via APIs.

6. Testing

    Simulate access attempts with valid and invalid codes.
    Test MQTT communication for delays and reliability.
    Validate encryption and data integrity using tools like Wireshark.
