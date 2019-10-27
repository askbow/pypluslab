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

cmds = [
'show version',
'show lldp neighbors',
]

for command in cmds:
    res = dev_conn.send_command(command, use_textfsm=True )
    if 'lldp' in command:
        print( type( res ) )
        print( res[0]['neighbor_interface'] )
    else:
        print( res[0]['version'] )

dev_conn.disconnect()

