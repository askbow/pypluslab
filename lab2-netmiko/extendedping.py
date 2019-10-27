from netmiko import ConnectHandler
from getpass import getpass


device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

dev_conn = ConnectHandler(**device)
print( dev_conn.find_prompt() )
