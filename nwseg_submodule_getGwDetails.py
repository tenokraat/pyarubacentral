
# Import Aruba Central Base
from pycentral.base import ArubaCentralBase
from pycentral.monitoring import Devices
from pprint import pprint


# Create the following files by refering to the samples.
central_filename = "input_credentials.yaml"

# Get instance of ArubaCentralBase from the central_filename
from pycentral.workflows.workflows_utils import get_conn_from_file
central = get_conn_from_file(filename=central_filename)

# Sample API call using Configuration sub-module `pycentral.configuration`

m = Devices()

module_resp = m.get_device_details(central, "MobilityController", "CG0046063")
pprint(module_resp)
