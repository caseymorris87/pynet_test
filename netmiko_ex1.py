#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

def main():

    cisco_pass = getpass('Please enter Cisco password: ')
    arista_pass = getpass('Please enter Arista password: ')

    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': cisco_pass
    }

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'admin1',
        'password': arista_pass
    }

    for con in (pynet_rtr1, pynet_sw1):
        net_connect = ConnectHandler(**con)
        print net_connect.find_prompt()
        print net_connect.send_command('show version')
        run = net_connect.send_command('show run')
        with open('netmiko_config_' + con['device_type'], 'w') as conffile:
            conffile.write(run)
        
if __name__ == '__main__':
    main()
