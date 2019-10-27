from netmiko import ConnectHandler
from getpass import getpass


device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

dev_conn = ConnectHandler(**device)
#print( dev_conn.find_prompt() )

output = dev_conn.send_command_timing('ping', strip_prompt=False, strip_command=False)
output += dev_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += dev_conn.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
while '#' not in output:
   output += dev_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)

print( output )
################
dev_conn.disconnect()

