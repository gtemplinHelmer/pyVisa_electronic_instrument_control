# implementation of BK Precision 8601B Control
import datetime
import os
import pyvisa   # Wrapper for VISA
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
    file_path = r'S:\Acadarch\TESTING\COMPLETE TEST FILES\1274\1274.007\Python Files\Discharge Data Collected'
    print("\nData will be stored in the following location: " + file_path)
    electronic_load = BK_Precision_8601B(file_path, resource_manager)   # create the electronic load object
    electronic_load.setup()  # let the user decide what they want the load to do during this run

    # this will contain all the run types
    if electronic_load.run_type == "MANUAL":
        electronic_load.run_manual()
    elif electronic_load.run_type == "FILE":
        electronic_load.run_file_mode()
    elif electronic_load.run_type == "BATTERY DISCHARGE":
        electronic_load.cc_til_discharged()
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
