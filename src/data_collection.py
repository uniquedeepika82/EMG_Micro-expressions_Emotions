#Collects EMG data from Arduino and stores it in a CSV file

import serial
import csv
from datetime import datetime

SUBJECT_ID = input("Enter subject ID (e.g., subject_01): ")
EMOTION = input("Enter emotion label (e.g., happy): ")
PORT = 'COM3'  
BAUD_RATE = 9600
DURATION = 10  # seconds to collect data per emotion

filename = f"d:/emg_micro/data/gen/emg_{SUBJECT_ID}_{EMOTION}.csv"

with serial.Serial(PORT, BAUD_RATE, timeout=1) as ser, open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp'] + [f'Channel_{i+1}' for i in range(8)])

    print(f"Collecting data for {DURATION} seconds...")
    start_time = datetime.now()

    while (datetime.now() - start_time).seconds < DURATION:
        line = ser.readline().decode('utf-8').strip()
        if line:
            values = line.split(',')
            if len(values) == 8:
                writer.writerow([datetime.now().isoformat()] + values)

print("Data collection complete.")
