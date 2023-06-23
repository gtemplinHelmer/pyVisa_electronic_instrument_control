# Parent class is template for control of electronic instruments in general
# BK_Precision class implements that specifically for BK Precision 8601B model

import pyvisa
import time
import pandas as pd
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


    def run_manual(self):
        print("Running manually")


    def run_file_mode(self):
        print("Getting info from the file")


    def choose_resource(self):
        resource_chosen = False
        while resource_chosen == False:
            # choose your resource
            print(self.resource_manager.list_resources())  # shows which resources are available
            self.resource_digital_location = input("Copy and paste the resource to use (not including single quotes): ")
            try:
                self.resource_object = self.resource_manager.open_resource(self.resource_digital_location)  # create an object from a resource at a particular digital location
                print("Load information: " + self.resource_object.query('*IDN?'))  # electronic load official name
                resource_chosen = True
            except:
                print("Something went wrong, try again")


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


    def direct_input(self, input_value):  # a direct input to change the equipment's functionality in the most basic way
        pass


    def read_from_csv(self, csv_file_name):  # what the load will do when reading values from a csv file
        pass


    def read_values(self):  # will return the given values for equipment, whatever that may mean
        pass

















