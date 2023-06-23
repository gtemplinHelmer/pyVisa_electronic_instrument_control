# Parent class is template for control of electronic instruments in general
# BK_Precision class implements that specifically for BK Precision 8601B model

import pyvisa
import time
import pandas as pd
import csv

from abc import ABC, abstractmethod



class ElectronicTestEquipment(ABC):  # Template class for any electronic load

    @abstractmethod
    def __init__(self):  # will define all parameters the equipment requires
        pass

    @abstractmethod
    def setup(self):  # will fill in the parameters based on user defined inputs
        pass

    @abstractmethod
    def direct_input(self, input_value):  # a direct input to change the equipment's functionality in the most basic way
        pass

    @abstractmethod
    def read_from_csv(self, csv_file_name):  # what the load will do when reading values from a csv file
        pass

    @abstractmethod
    def read_values(self):  # will return the given values for equipment, whatever that may mean
        pass


class BK_Precision_8601B(ElectronicTestEquipment):
    # Needs a resource manager object from pyVisa
    # Needs a load output address to talk to via usb or some other output configuration

    def __init__(self, storage_file, resource_manager):
        self.data_storage_location = storage_file   # likely a CSV file
        self.resource_manager = resource_manager    # pyVisa object
        self.run_type = "Undefined"   # describes what type of testing is done (manual control, read from file, etc)
        self.resource_digital_location = "No resource yet"
        self.resource_object = None  # nonexistent until user inputs




    # find the digital location of the load
    def setup(self):
        self.choose_resource()
        # user decides what to do with the resource
        print("Choose how to use the load")
        user_choice = "No choice yet"
        while user_choice == "No choice yet":
            user_choice = str.upper(input("Enter 'manual' for manual use, or enter 'file' to control load from a CSV file: "))
            if user_choice == "MANUAL":
                self.run_type = user_choice
            elif user_choice == "FILE":
                self.run_type = user_choice
            else:
                print("Not a choice")
        # create genuine resource object that commands will be written to and queried from
        self.resource_object = self.resource_manager.open_resource(self.resource_digital_location)
        print("Your chosen equipment identification: " + self.resource_object.query('*IDN?'))  # electronic load official name


    def choose_resource(self):
        resource_chosen = False
        while resource_chosen == False:
            # choose your resource
            print(self.resource_manager.list_resources())  # shows which resources are available
            self.resource_digital_location = input("Copy and paste the resource to use (not including single quotes): ")
            try:
                self.resource_object = self.resource_manager.open_resource(
                    self.resource_digital_location)  # create an object from a resource at a particular digital location
                print("Load information: " + self.resource_object.query('*IDN?'))  # electronic load official name
                self.resource_object.write("SYSTEM:REMOTE")  # give the computer control over the load
                self.resource_object.write("INPUT OFF")  # initially the source is off
                resource_chosen = True
            except:
                print("Something went wrong, try again")


    def run_manual(self):
        print("Running manually")
        self.user_choose_mode()  # user decides if CC, CV, CW, or CR should be used
        time_interval = self.set_interval()
        measurement_range = self.set_range()  # how many total intervals to measure from
        total_seconds = time_interval * measurement_range
        total_minutes = float(total_seconds / 60)
        print("This experiment will run for " + total_minutes + " minutes")
        load_level = input("Enter the input magnitude you would like")  # user specifies the current, voltage, power, or resistance level they would like

        input("Press enter to start measuring (this will turn on the load, so be careful)")
        self.resource_object.write("Input ON")  # turn the electronic load on. we are now live
        voltage = 0
        current = 0
        data = []
        for index in range(measurement_range):  # measure current and voltage, and upload these to a CSV file
            voltage = self.resource_object.query(":FETCH:VOLTAGE?")
            current = self.resource_object.query(":FETCH:CURRENT?")
            power = voltage * current
            data.append(voltage, current, power)
            time.sleep(time_interval)
        # format and store the collected data
        data_frame = pd.DataFrame(data, columns=['Voltage', 'Current', 'Power'])
        data_frame.to_csv(self.data_storage_location)


    @staticmethod
    def set_range(self) -> int:
        while True:
            print(
                "How many measurements do you want to take?")
            try:
                range = int(input("Enter an integer: "))
                break
            except ValueError:
                print("Enter just the integer")
        return range


    @staticmethod
    def set_interval(self) -> int:
        while True:
            print("What do you want your interval between measurements to be? Voltage and current measurements will be given")
            try:
                interval = int(input("Enter an integer: "))
                break
            except ValueError:
                print("Enter just the integer")
        return interval


    def user_choose_mode(self):
        continuing = True
        while continuing:
            print("Would you like CC, CV, CW, or CR? ")
            load_mode = input("Enter one of the options: ")
            if str.upper(load_mode) == "CC":
                self.resource_object.write("FUNC CURR")
                continuing = False
            elif str.upper(load_mode) == "CV":
                self.resource_object.write("FUNC VOLT")
                continuing = False
            elif str.upper(load_mode) == "CW":
                self.resource_object.write("FUNC POW")
                continuing = False
            elif str.upper(load_mode) == "CR":
                self.resource_object.write("FUNC RES")
                continuing = False
            else:
                print("Invalid choice")




    def run_file_mode(self):
        print("Getting info from the file")

    def direct_input(self, input_value):  # a direct input to change the equipment's functionality in the most basic way
        pass


    def read_from_csv(self, csv_file_name):  # what the load will do when reading values from a csv file
        pass


    def read_values(self):  # will return the given values for equipment, whatever that may mean
        pass

















