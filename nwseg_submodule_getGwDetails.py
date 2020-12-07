
# Import Aruba Central Base
from pycentral.base import ArubaCentralBase
from pycentral.configuration import Groups
from pycentral.monitoring import Devices
from pprint import pprint
import json


# Create the following files by refering to the samples.
central_filename = "input_credentials.yaml"

# Get instance of ArubaCentralBase from the central_filename
from pycentral.workflows.workflows_utils import get_conn_from_file
central = get_conn_from_file(filename=central_filename)

g = Groups()
d = Devices()

groups = g.get_groups(central)

#pprint(groups)
print(groups['msg']['data'])

group_names = groups['msg']['data']
print(type(group_names))


#for group, group_name in groups.items():
#    print("\Group-Name", group)
for key, value in group_dict.items():
    print(key, '->', value)


#device_details = d.get_device_details(central, "mobility_controllers", "CG0046063")
#print(device_details['msg']['group_name'])

#with open('gw-details.json', 'w') as file1:
#    file1.write(json.dumps(device_details))

