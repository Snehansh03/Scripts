#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", dest="interface", help="Input the interface")
    parser.add_option("-m", dest="mac_address", help="Input the mac_address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please enter the interface, use --help for info")
    elif not options.mac_address:
        parser.error("[-] please enter the mac, use --help for info")
    return options

def change_mac(interface,mac_address):
    print("[+] Changing Mac Address for "+interface+" to " + mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def get_currentMac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", interface])
    search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result.decode())
    if search_result:
        return search_result.group(0)
    else:
        print("[-] Could not read MAC")

options=get_arguments()
current_mac=get_currentMac(options.interface)
print("[+] Current Mac "+ str(current_mac))
change_mac(options.interface,options.mac_address)
current_mac=get_currentMac(options.interface)
if current_mac == options.mac_address:
    print("[+] MAC changed successfully to "+current_mac)
else:
    print("[-] MAC did not change")




