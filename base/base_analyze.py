import os

import yaml

def analyze_file(file_name,data_key):
    with open("../data/" + file_name,"r" ) as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        dict_data = data[data_key]
        list_data = []
        for i in dict_data.values():
            list_data.append(i)
        print(list_data)
analyze_file("contact_data.yaml","test_contact")