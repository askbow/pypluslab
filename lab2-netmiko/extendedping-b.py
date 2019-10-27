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


dialog = [r'Protocol',
r'Target IP',
r'Repeat count',
r'Datagram size',
r'Timeout in seconds',
r'Extended commands',
r'Sweep range of sizes', r'#',] 

output = ""

for d in dialog:
    PROMPT = False
    if 'Repeat' in d :
        command = "8.8.8.8"
    elif 'Protocol' in d:
        command= "ping"
        PROMPT = True
    else:
        command = "\n"
    #print("sending\t",command,'\texpecting',d)
    print( dev_conn.send_command(command, expect_string=d, 
              strip_prompt=PROMPT, strip_command=False) )

dev_conn.disconnect()

