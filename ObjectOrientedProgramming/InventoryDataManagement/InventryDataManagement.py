import json


# Read the JSON file and display data of file
def read_File():
    # open file and read data from file
    with open("inventory.json", 'r') as json_file:
        # load the file data into a variable data
        data = (json.load(json_file))
        return data

# print all file data line by line

def print_data(data):
    print('\nData of file is following : \n')
    for elements, value in data.items():
        print(elements, end='\n')
        for list_item in value:
            for attribute1, attribute2 in list_item.items():
                print('\t: ', attribute1, ' = ', attribute2)


# take the price and weight value and print total price of stock inventory
def print_total_price(data):
    for elements, value in data.items():
        total_price = 0
        for list_item in value:
            weight = 0
            price = 0
            for attribute1, attribute2 in list_item.items():
                if attribute1 == 'weight':
                    weight = attribute2
                if attribute1 == 'price':
                    price = attribute2
            total_price += weight * price
        print('Total price of stock : ', elements, 'is : ', total_price)