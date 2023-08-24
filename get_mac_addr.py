#!/usr/bin/python3



import sys
import json
import requests
from proxmoxer import ProxmoxAPI
import re



def fetch_vm_network_info(vm_id):
    proxmox = ProxmoxAPI('192.168.122.109:8006', user='root@pam', password='@ali.1397', verify_ssl=False)
    config = proxmox.nodes("ali").qemu(101).config.get()
    net= config['net0']
    mac_addr = re.split(r'[=,]',net)


    return mac_addr[1]
    



vm_id = 101
mac_address = fetch_vm_network_info(vm_id)
print(json.dumps({'mac_address': mac_address}))
#71b481ee-fdd6-4148-84e1-e9646a3a19b5