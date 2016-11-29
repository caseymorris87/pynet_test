#!/usr/bin/env python

import devices
from netmiko import ConnectHandler
from pprint import pprint
import threading
from queue import Queue

def show_arp(dev, outq):
    conn = ConnectHandler(**dev)
    output = '#' * 80 + '\n'
    output += conn.send_command('show arp') + '\n'
    output += '#' * 80 + '\n'
    outq.put(output)

def main():

    outq = Queue(maxsize=20)

    for dev in devices.devs:
        my_thread = threading.Thread(target=show_arp, args=(dev, outq))
        my_thread.start()
    main_thread = threading.currentThread()
    for athread in threading.enumerate():
        if athread != main_thread:
            athread.join()

    while not outq.empty():
        print outq.get()

if __name__ == '__main__':
    main()
