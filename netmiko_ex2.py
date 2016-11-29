#!/usr/bin/env python

from netmiko import ConnectHandler

def main():
    cmd_vlan = ['vlan 100', 'name from-cmd', 'end']
    file_vlan = 'file_vlan'

    info = {
        'device_type': 'arista_eos',
        'ip': '184.105.247.72',
        'username': 'admin1',
        'password': '99saturday'
    }

    net_connect = ConnectHandler(**info)

    net_connect.send_config_set(cmd_vlan)
    net_connect.send_config_from_file(file_vlan)

if __name__ == '__main__':
    main()
