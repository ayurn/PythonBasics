import json
import re

from pip._internal.utils import logging

import loggerfile

# Address book class here require all information of any person
class AddressBook:

    def __init__(self):
        # initially all entry are None (or default)
        self.details = {
            'first_name': None,
            'last_name': None,
            'address': None,
            'city': None,
            'state': None,
            'zip_code': 0,
            'phone_number': 0
        }


class MenuBar():

    # Method for add new person in the address book
    def add_new_person(self):

        """
        Description:
            Function to add new person to contact.
        Return:
            details of the contact
        """

        details = {}

        try:
            while True:
                f_name = input('Enter your first name ')
                Pattern = re.compile("[A-Za-z]{2,25}")
                if (re.match(Pattern, f_name, flags=0)):
                    break
                else:
                    print("Enter valid first name.")

            while True:
                l_name = input('Enter your last name ')
                Pattern = re.compile("[A-Za-z]{2,25}")
                if (re.match(Pattern, l_name, flags=0)):
                    break
                else:
                    print("Enter valid last name.")

            address = input('Enter your Address ')

            city_name = input('Enter your city name ')

            while True:
                state_name = input('Enter your state ')
                Pattern = re.compile("[A-Za-z]{2,25}")
                if (re.match(Pattern, state_name, flags=0)):
                    break
                else:
                    print("Enter valid State.")

            while True:
                zip_code = input('Enter your city zip ')

                if (re.match(r'^(\d{4}|\d{6})$', zip_code, flags=0)):
                    break
                else:
                    print('zip code should be in 6 digits ')

            while True:
                mobile_no = input('Enter your phone number ')
                Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
                if (re.match(Pattern, mobile_no, flags=0)):
                    break
                else:
                    print('please valid mobile number( mobile number should have 10 digits and first digit should be '
                          'start with 7,8 or 9)')

            #details['first_name'] = f_name
            details['first_name'] = f_name
            details['last_name'] = l_name
            details['address'] = address
            details['city'] = city_name
            details['state'] = state_name
            details['zip_code'] = zip_code
            details['phone_number'] = mobile_no
        except Exception as e:
            loggerfile.Logger("error", (print(e)))
        finally:
            return details

    # Edit the person details based on person first name if person does not
    # want to edit some details the enter same as previous
    def edit_information(self, name):

        """
        Description:
            Function to edit existing contacts
        Parameters:
            name of the person whose contact we have to edit.
        """
        try:
            flag = True
            for i in book:
                if i['first_name'] == name:
                    flag = False
                    i['address'] = input('Edit your Address ')
                    i['city'] = input('Edit your city name ')
                    i['state'] = input('Edit your state ')
                    i['zip_code'] = int(input('Edit your city zip '))
                    i['phone_number'] = int(input('Edit your phone number '))
                    break
            if flag:
                print('this name is not present in the address book')
        except Exception as e:
            loggerfile.Logger("error", (print(e)))

    # Delete a person from the address book
    def delete_person(self, name):

        """
        Description:
            Function to delete existing contacts
        Parameters:
            name of the person whose contact we have to delete.
        """
        try:
            flag = True

            for i in book:
                if i['first_name'] == name:
                    flag = False
                    book.remove(i)
            if flag:
                print('this name is not present in the address book')
        except Exception as e:
            loggerfile.Logger("error", (print(e)))

    # sort the all address book detail based on the address

    def sort_by_address(self):

        """
        Description:
            Function to sort contacts by address.
        """
        try:
            addr = []

            for i in book:
                addr.append(i['address'])

            addr = sorted(addr, key=lambda s: s.casefold())

            print(' %15s %15s %15s %15s %15s %15s %15s' % (
                'First name', 'Last name', 'Address', 'City', 'State', 'Zip', 'Phone number'))
            print(
                '------------------------------------------------------------------------------------------------------------------------')

            for i in addr:
                for j in book:
                    if j['address'] == i:
                        print(' %15s %15s %15s %15s %15s %15s %15s' % (
                            j['first_name'], j['last_name'], j['address'], j['city'], j['state'], j['zip_code'],
                            j['phone_number']))
                        break
        except Exception as e:
            loggerfile.Logger("error", (print(e)))

    # sort the all address book detail based on the first name
    def sort_by_name(self):

        """
        Description:
            Function to sort contacts by name.
        """
        addr = []
        try:
            for i in book:
                addr.append(i['first_name'])

            addr = sorted(addr, key=lambda s: s.lower())

            print(' %15s %15s %15s %15s %15s %15s %15s' % (
                'First name', 'Last nmae', 'Address', 'City', 'State', 'Zip', 'Phone number'))
            print(
                '--------------------------------------------------------------------------------------------------------------------')

            for i in addr:
                for j in book:
                    if j['first_name'] == i:
                        print(' %15s %15s %15s %15s %15s %15s %15s' % (
                            j['first_name'], j['last_name'], j['address'], j['city'], j['state'], j['zip_code'],
                            j['phone_number']))
                        # print(j['first_name']," : ",j['last_name']," : ",j['address']," : ",j['city' ]," : ",j['state'
                        # ]," : ",j['zip_code']," : ",j['phone_number'] )
                        break
        except Exception as e:
            loggerfile.Logger("error", (print(e)))

    # sort the all address book detail based on the zip code
    def sort_by_zip(self):

        """
        Description:
            Function to sort contacts by zip.
        """
        try:
            addr = []

            for i in book:
                addr.append(i['zip_code'])

            addr.sort()

            print(' %15s %15s %15s %15s %15s %15s %15s' % (
                'First name', 'Last nmae', 'Address', 'City', 'State', 'Zip', 'Phone number'))
            print(
                '---------------------------------------------------------------------------------------------------------------------')

            for i in addr:
                for j in book:
                    if j['zip_code'] == i:
                        print(' %15s %15s %15s %15s %15s %15s %15s' % (
                            j['first_name'], j['last_name'], j['address'], j['city'], j['state'], j['zip_code'],
                            j['phone_number']))
                        break
        except Exception as e:
            loggerfile.Logger("error", (print(e)))

    # save all person derails into file
    def save(self, data):

        """
        Description:
            Function to save contacts.
        Parameters:
            data of contact.
        """
        with open('Address_book.json', 'w') as AB:
            json.dump(data, AB, indent=1)

# Read the address book file
def read_File():
    # open file and read data from file
    with open("Address_book.json", 'r') as json_file:
        # load the file data into a variable data
        data = (json.load(json_file))
        return data

book = read_File()

