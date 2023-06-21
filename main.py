# implementation of BK Precision 8601B Control

import sys
import signal
import time

import pyvisa   # Wrapper for VISA
import pandas   # Read from CSV, save captured data to another CSV
import csv  # to create CSV file to store data in

from instrument_control import BK_Precision_8601B  # the load I am using



def interrupt_handler(signum, frame):
    print(f'Handling signal {signum} ({signal.Signals(signum).name}).')
    print("Saving data")
    #   Turn off the load code
    #   Save the current data code
    print("Done")
    sys.exit(0)  # terminate the program


def main():
    print("Starting program")
    print("Press Ctr1+F2 (Windows) or Ctrl+C (Linux) to terminate the program ")

    resource_manager = pyvisa.ResourceManager()  # object managing all possible test equipment attached
    print(resource_manager.list_resources())  # shows connections to equipment
    resource_location = input("Copy and paste the resource to use (not including single quotes): ")  # shows digital 'location' (USB, RS-32, etc)

    file_name = input("Input a file name and location for your data to be stored")
    equipment = BK_Precision_8601B(file_name)
    file = open(file_name, "x")


    time.sleep(60)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, interrupt_handler)
    main()
