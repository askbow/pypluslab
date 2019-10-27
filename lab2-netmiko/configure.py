from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

dev_conn = ConnectHandler(**device)
#print( dev_conn.find_prompt() )

cmds = [
'ip name-server 1.1.1.1',
'ip name-server 1.0.0.1',
'ip domain-lookup',
]

def verping(dev_conn):
   ping = dev_conn.send_command('ping google.com')
   if '!' in ping:
       return "ping OK"
   else:
       return "ping FAIL"


print("="*10, "SLOW", "="*10)
start = datetime.now()
print("pre-config validation", verping(dev_conn) )
# configure
conf = dev_conn.send_config_set(cmds)
print("post-config validation", verping(dev_conn) )
#unconfigure
anticmds = [ "no "+c for c in cmds ]
conf = dev_conn.send_config_set(anticmds)
print("un-config validation", verping(dev_conn) )
dev_conn.disconnect()
print("\n\tIt took us",datetime.now() - start )

device['fast_cli'] = True
dev_conn = ConnectHandler(**device)
print("="*10, "FAST", "="*10)
start = datetime.now()
print("pre-config validation", verping(dev_conn) )
# configure
conf = dev_conn.send_config_set(cmds)
print("post-config validation", verping(dev_conn) )
#unconfigure
anticmds = [ "no "+c for c in cmds ]
conf = dev_conn.send_config_set(anticmds)
print("un-config validation", verping(dev_conn) )
dev_conn.disconnect()
print("\n\tIt took us",datetime.now() - start )
