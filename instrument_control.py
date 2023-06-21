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


    # Needs a resource manager object from pyVisa
    # Needs a load output address to talk to via usb or some other output configuration
class BK_Precision_8601B(ElectronicTestEquipment):

    def __init__(self, storage_file):
        self.data_storage_location = storage_file   # likely a CSV file

    # def setup(self):









