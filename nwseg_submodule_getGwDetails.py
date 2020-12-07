
# Import Aruba Central Base
from pycentral.base import ArubaCentralBase
from pycentral.configuration import Groups
from pycentral.monitoring import Devices
from pprint import pprint
import json
import csv
import pandas
import collections


# Create the following files by refering to the samples.
central_filename = "input_credentials.yaml"

# Get instance of ArubaCentralBase from the central_filename
from pycentral.workflows.workflows_utils import get_conn_from_file
central = get_conn_from_file(filename=central_filename)

g = Groups()
d = Devices()

#Import gateway export CSV to pandas DataFrame

df = pandas.read_csv('export_gateway_list_dev.csv', index_col='Device Name')

print ('Entire pandas DataFrame:')
print(df)

for index in df.index:

    uptime = df['Uptime'][index]
    group = df['Group'][index]

    if  uptime != '0:00:00' and group == 'CH-HS-BNC_LAB':

        mac_addr = df['MAC'][index]
        print(mac_addr)
        serial = df['Serial'][index]
        print(serial)

        #device_details = d.get_device_details(central, 'mobility_controllers', f'{serial}')
        #print(device_details['msg'])
        #print(type(device_details))

        uplink_details = d.get_gateway_uplink_details(central, 'mobility_controllers', f'{serial}', '3H')

        uplinks = uplink_details['msg']['uplinks']
        print (type(uplinks))

        keys = uplink_details['msg'].keys()
        values = uplink_details['msg'].values()

        #print(keys)
        #print(values)

        values_list = list(values)

        #print(values_list[10])
        #print(type(values_list))

        #print(uplink_details['msg'][1])


        
        


#pprint(gateway_dict)

#with open('gw-details.json', 'w') as file1:
#    file1.write(json.dumps(device_details))

