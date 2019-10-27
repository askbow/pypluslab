from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}

dev_conn = ConnectHandler(**device)


command = 'show lldp neighbors detail'
start = datetime.now()
output = dev_conn.send_command(command)
end = datetime.now()
output += "\nCompleted in {}".format(end-start)
output += "\n"

# with delay:
start = datetime.now()
output += dev_conn.send_command(command, delay_factor = 8)
end = datetime.now()
output += "\nCompleted in {} with delay".format(end-start)
output += "\n"

print(output)
