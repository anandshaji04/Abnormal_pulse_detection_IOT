# Pulse Monitoring System with Abnormality Detection

## Project Overview
This project aims to create a pulse monitoring system with abnormality detection using a heart rate sensor module, Arduino, Bolt WiFi module, and cloud services like Mailgun and Twilio. The system collects data from the heart rate sensor module, calculates heart rate, and sends alerts via email and SMS when abnormal readings are detected.

## Hardware Setup
1. **Connecting Heart Rate Sensor to Arduino**: Connect pin 2 of Arduino to the output pin of the heart rate sensor module, 5V pin of Arduino to VCC pin of the sensor module, and GND pin of Arduino to GND pin of the sensor module.
2. **Coding in Arduino**: Write and upload code to Arduino to collect data from the sensor module and calculate heart rate.
3. **Connecting Bolt WiFi Module to Arduino**: Connect 3V3 pin of the Bolt WiFi module to 3.3V pin of Arduino, TX pin of Bolt module to RX pin of Arduino, and RX pin of Bolt module to TX pin of Arduino.

## Software Setup
4. **Setting up Email Automation using Mailgun**: Create an account on Mailgun, add recipient email, and obtain necessary credentials for sending emails.
5. **Setting up SMS Service using Twilio**: Sign up on Twilio, enable SMS services, obtain Account SID, Auth token, and phone number.
6. **Using DigitalOcean VPS for Running Code**: Create a droplet running Ubuntu on DigitalOcean, access it using PuTTY, and run the heart rate monitoring code.

## Repository Content
- **Arduino Code**: Arduino code for collecting data from the heart rate sensor module and communicating with the Bolt WiFi module.
- **Python Code**: Python code for processing data, detecting abnormalities, and sending email and SMS alerts.
- **Readme File**: Instructions for setting up the hardware, software, and cloud services, along with project overview and repository content.
