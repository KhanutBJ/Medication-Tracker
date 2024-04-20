import serial
import requests
import time
import random

# Open serial connection to Arduino UNO
# ser = serial.Serial('/dev/cu.usbserial', 10)  # Adjust port name based on your system
print("Serial connection established")
print('='*50)
# Function to parse RFID data and send notification
def process_RFID_data(data):
    # Split RFID data into individual fields
    medication_info = data.split(',')

    # Extract medication information
    status = medication_info[0]
    drug_name = medication_info[1]
    num_capsules = int(medication_info[2])
    time_to_take = medication_info[3]

    # Print medication information
    print("Status:", status)
    print("Drug Name:", drug_name)
    print("Number of Capsules Required:", num_capsules)
    print("Time to Take:", time_to_take)
    
    # Send notification to web application
    send_notification(status, drug_name, num_capsules, time_to_take)

# Function to send notification to web application
def send_notification(status, drug_name, num_capsules, time_to_take):
    # Sample code to send HTTP POST request to web application
    url = "http://127.0.0.1:5000/notification"
    payload = {
        "status": status,
        "drug_name": drug_name,
        "num_capsules": num_capsules,
        "time_to_take": time_to_take
    }
    
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    print("Notification sent to web application")
    print('*'*50)
# Main loop to continuously read data from Arduino UNO
while True:
    # if ser.in_waiting > 0:
        # Read RFID data from Arduino UNO
        # data = ser.readline().decode().strip()
        
        data = 'due,Paracetamol,2,every 1 hours'
        
        print("RFID Data:", data)

        # Process RFID data
        process_RFID_data(data)
        
        interval = 10
        # interval = random.choice([20,40,60,80])
        time.sleep(interval)
        
        print(f"time interval between pill taking: {interval} seconds")
