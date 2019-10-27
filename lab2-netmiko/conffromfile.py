from netmiko import ConnectHandler
from getpass import getpass


def main():
    password = getpass()
    devices = [ {'host': 'nxos'+str(n)+'.lasthop.io', 
    'username':'pyclass','password':password,
    'device_type':'cisco_nxos',} for n in range(1,3) ]
    for d in devices:
        print(d['host'])
        with ConnectHandler( **d ) as dev:
            res = dev.send_config_from_file("vlans.txt")
            print("="*20,"\n"*2,res,"\n"*2,"="*20,"\n")
            dev.save_config()



if __name__== "__main__":
    main()
