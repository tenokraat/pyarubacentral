
# Import Aruba Central Base
from pycentral.configuration import Groups
from pprint import pprint
import json
import requests

# Create the following files by refering to the samples.
central_filename = "input_credentials.yaml"

# Get instance of ArubaCentralBase from the central_filename
from pycentral.workflows.workflows_utils import get_conn_from_file
central = get_conn_from_file(filename=central_filename)

# Get groups max limit 20, apply offset and fetch other groups in loop
g = Groups()

module_resp = g.get_groups(central)

print(type(module_resp))

group_json = json.dumps(module_resp)

print(group_json)

group_data = json.loads (group_json)

for group in group_data:
    print(group[0])

print(group_data)

print("DONE")
