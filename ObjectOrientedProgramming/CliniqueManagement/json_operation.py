import os
import sys
import json
def load_data_doctor():
    """
        Description:
            this method define for load data from doctor.json file
        Parameter:
            None
        Return:
            data (dict) : load data of json file
    """
    with open(os.path.abspath('json/doctor.json'),'r') as jsonfile:
        data_doctor = json.load(jsonfile)
        jsonfile.close()
    return data_doctor

def load_data_patient():
    """
        Description:
            this method define for load data from doctor.json file
        Parameter:
            None
        Return:
            data (dict) : load data of json file
    """
    with open(os.path.abspath('json/patient.json'),'r') as jsonfile:
        data_patient = json.load(jsonfile)
        jsonfile.close()
    return data_patient

def load_data_appoitment():
    """
        Description:
            this method define for load data from doctor.json file
        Parameter:
            None
        Return:
            data (dict) : load data of json file
    """
    #Clinique_Management_Programme/json/appointement_servey.json
    with open(os.path.abspath('json/appointement_servey.json'),'r') as jsonfile:
        data_appointent = json.load(jsonfile)
        jsonfile.close()
    return data_appointent

def upload_data_appoitment(data_appointent):
    """
        Description:
            this method define for upload data into json file
        Parameter:
           data (dict) : loaded data from json file
        Return:
            None
    """
    with open(os.path.abspath('json/appointement_servey.json'),'w') as jsonfile:
        json.dump(data_appointent,jsonfile,indent=3)
        jsonfile.close()