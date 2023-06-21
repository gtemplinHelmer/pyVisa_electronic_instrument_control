# implementation of BK Precision 8601B Control

import sys
import signal
import time

import pyvisa   # Wrapper for VISA
import pandas   # Read from CSV, save captured data to another CSV


def interrupt_handler(signum, frame):
    print(f'Handling signal {signum} ({signal.Signals(signum).name}).')
    print("Saving data")
    time.sleep(2)
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

    #  create equipment object based on what the user inputs (electronic load, function generator, etc)

    time.sleep(60)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, interrupt_handler)
    main()
