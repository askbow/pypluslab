from netmiko import ConnectHandler
from getpass import getpass
import time


PASS = getpass()
device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": PASS,
    "secret": PASS,
    "device_type": 'cisco_ios',
    "session_log": 'cisco4_output.txt',
}

dev_conn = ConnectHandler(**device)
print( dev_conn.find_prompt() )
dev_conn.config_mode()
print( dev_conn.find_prompt() )
dev_conn.exit_config_mode()
print( dev_conn.find_prompt() )
dev_conn.write_channel('disable\n')
time.sleep(2)
print( dev_conn.read_channel() )
dev_conn.enable()
print( dev_conn.find_prompt() )
dev_conn.disconnect()

