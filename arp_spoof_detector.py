# Python Final PY-07-L1 6/23/23 (last modified 6/26/23)

"""
You suspect the network is under an On-Path attack.
You need to create a script that automatically identifies ARP Spoofing behavior on
workstations.
"""

import os   # It lets you start new applications right from the Python program you are currently writing
import datetime
import time

def extract_arp_table():
    # Execute the command to retrieve the ARP table
    command = "arp -a"  # Command to retrieve ARP table
    arp_output = os.popen(command).read()


    # Split the output into separate lines
    lines = arp_output.splitlines()

    # Filter and process the data to extract IP and MAC addresses
    filtered_data = {}
    for line in lines:
        if "dynamic" in line:
            parts = line.split()

            ip_address = parts[0]
            mac_address = parts[1]
            filtered_data[ip_address] = mac_address

    return filtered_data



# TASK 2

def identify_mac_duplication(filtered_data):
    recorded_macs = []

    for mac in filtered_data.values():
        if mac in recorded_macs:
            print("Duplicate MAC address identified:",(mac))
            log_arp_spoofing_event(mac)

            break
        recorded_macs.append(mac)

# TASK 3

def log_arp_spoofing_event(event_data):
    # Create a variable to store the date and time of the event
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a timestamp and event data
    log_message = "[{}] ARP Spoofing Event: {}".format(timestamp, event_data)

    # Save the logged data to a file
    with open("arp_spoofing.log", "a") as file:
        file.write(log_message + "\n")

if __name__ == "__main__":
    while True:
        filtered_data = extract_arp_table()
        print(filtered_data)

        identify_mac_duplication(filtered_data)
        print("Script executed successfully.")
        time.sleep(5)