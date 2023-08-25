#!/usr/bin/python3



import sys
import json
from proxmoxer import ProxmoxAPI
import re



def fetch_vm_network_info():
    all_mac_addresses = {}
    proxmox = ProxmoxAPI('192.168.122.109:8006', user='root@pam', password='@ali.1397', verify_ssl=False)
    
    vm_details = proxmox.nodes("ali").qemu.get()
    vm_ids = [vm_id['vmid'] for vm_id in vm_details if vm_id['vmid']!= 100 ]
    for vm_id in vm_ids:

        config = proxmox.nodes("ali").qemu(vm_id).config.get()
        net= config['net0']
        virtio = re.split(r'[=,]',net)
        mac_address  = virtio[1]

        all_mac_addresses[vm_id] = mac_address

    return all_mac_addresses
    



result = fetch_vm_network_info()   
print(json.dumps(result))
#71b481ee-fdd6-4148-84e1-e9646a3a19b5