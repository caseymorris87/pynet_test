#!/usr/bin/env python

import re
from pprint import pprint

def get_vendor(output):
    match = re.search(r'Cisco', output)
    return match.group(0)

def get_model(output):
    match = re.search(r'Cisco\s(\d+)\s', output)
    return match.group(1)

def get_version(output):
    match = re.search(r'Version (\d\d\.\d)', output)
    return match.group(1)

def get_serial(output):
    match = re.search(r'CISCO881-SEC-K9\s{7}(\w+)', output)    
    return match.group(1)

def get_uptime(output):
    match = re.search(r'uptime\sis\s(.+)', output)
    return match.group(1)

def main():
    with open('show_version.txt') as txtfile:
        output = txtfile.read()
    info = {}
    info['vendor'] = get_vendor(output)
    info['model'] = get_model(output)
    info['version'] = get_version(output)
    info['serial'] = get_serial(output)
    info['uptime'] = get_uptime(output)
    
    pprint(info)

if __name__ == '__main__':
    main()
