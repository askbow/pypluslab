#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device = {
"host"    : "cisco3.lasthop.io",
"device_type" : "cisco_ios",
"username"    : "pyclass",
"password"    : getpass(),
}


nc = ConnectHandler( **device )

print( nc.find_prompt() )
