#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

devices = [ {"host"    : "nxos" +x+".lasthop.io",
"device_type" : "cisco_nxos", "username"    : "pyclass",
"password"    : getpass(), }  for x in ("1","2") ]

for d in devices:
    nc = ConnectHandler( **d )
    print( nc.find_prompt() )
