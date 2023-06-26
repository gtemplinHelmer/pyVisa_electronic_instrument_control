# implementation of BK Precision 8601B Control
import datetime
import sys
import signal
import time
import os

import pyvisa   # Wrapper for VISA
import pandas   # Read from CSV, save captured data to another CSV
import csv  # to create CSV file to store data in

from instrument_control import BK_Precision_8601B  # the load I am using


'''
def interrupt_handler(signum, frame):
    print(f'Handling signal {signum} ({signal.Signals(signum).name}).')

    save_data()  # turn off the load and save what data you have
    print("Done")
    sys.exit(0)  # terminate the program
'''


def run_load():
    resource_manager = pyvisa.ResourceManager()  # object managing all possible test equipment attached
    storage_file_name = 'stored_data_' + formatted_datetime + '.csv'  # the csv file that data will be written to on this test
    current_path = os.path.dirname(os.path.abspath(__file__))  # get the path the file is currently in
    file_path = os.path.join(current_path, storage_file_name)  # what is the file path of the added CSV for storage
    print("\nData will be stored in the following location: " + file_path)
    print("This location should be the same folder that this program is stored in\n")
    electronic_load = BK_Precision_8601B(file_path, resource_manager)   # create the electronic load object
    electronic_load.setup()  # let the user decide what they want the load to do during this run

    # this will contain all the run types
    if electronic_load.run_type == "MANUAL":
        electronic_load.run_manual()
    elif electronic_load.run_type == "FILE":
        electronic_load.run_file_mode()
    else:
        print("Something went wrong")


def main():
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Format the date and time as a string
    global formatted_datetime
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    run_load()   # figure out what you are doing



if __name__ == '__main__':
    # signal.signal(signal.SIGINT, interrupt_handler)
    main()
