import csv
import math
import time
import random
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


####################################################################################
# Function name: get_data
# Function Description: This function reads data from external xml file
# Function Parameters: String - node (tag) name
# Function Return: String - node (tag value)
####################################################################################
def get_data(node_name):
    root = ET.parse('C:/AutomationFinal/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


####################################################################################
# Function name: wait
# Function Description: This function defines the waiting for elements until they presence or visible
# Function Parameters: String - element status (exist or displayed), Tuple - contain the element details
####################################################################################
def wait(for_element, elem):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located((elem[0], elem[1])))


####################################################################################
# Function name: read_csv
# Function Description: This function reads data from external csv file
# Function Parameters: String - file name
# Function Return: List - of the file data
####################################################################################
def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        data = [tuple(row) for row in reader]
        return data

# -------option 2--------:
# def read_csv(file_name):
#     data = []
#     with open(file_name, newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             data.insert(len(data), row)
#         return data


####################################################################################
# Function name: get_time_stamp
# Function Description: Returning the time for the pytest_exception_interact method in conftest file
# Function Return: float - the time of the system in seconds
####################################################################################
def get_time_stamp():
    return time.time()


# Enum for selecting displayed element or exist element, my wait method uses this enum
class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'


# Enum for selecting whether we want to save mortgage transaction or not
class Save:
    YES = True
    NO = False


# Enum for selecting the mobile swipe direction
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'


####################################################################################
# Function name: get_random_place
# Function Description: This function get  number and return a random number between 0 to the max number
# Function Parameters: Int - maximum number
# Function Return: Int - random number
####################################################################################
def get_random_place(max_num):
    start_place = 0
    my_random = math.floor(random.uniform(start_place, max_num-1))
    if my_random < 0:
        return 0
    elif my_random > max_num-1:
        return max_num-1
    return my_random

