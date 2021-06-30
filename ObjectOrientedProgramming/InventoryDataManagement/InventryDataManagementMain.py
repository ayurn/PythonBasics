"""
@Author: Ayur Ninawe
@Date: 2021-06-30 20:10:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-30 20:10:30
@Title : Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.
"""

# Program for read the data from json file and print all data

import InventryDataManagement as jsonObj

if __name__ == "__main__":
    data = jsonObj.read_File()
    jsonObj.print_data(data)
    jsonObj.print_total_price(data)