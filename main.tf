terraform {
  required_providers {
    proxmox = {
      source = "Telmate/proxmox"
      version = "2.9.14"
    }
  }
}

provider "proxmox" {
  # Configuration options
  pm_api_url="https://192.168.122.109:8006/api2/json"
  pm_user= "terraform-prov@pve"
  pm_password= "@ali.1397"
  pm_debug=true

}

resource "proxmox_vm_qemu" "Testing-Server-2" {
    count = 2
    target_node = "ali"
    clone = "new"
    full_clone = true
    memory = 1024
    onboot = true


 
}

data "external" "example" {
  depends_on = [ proxmox_vm_qemu.Testing-Server-2 ]
  program = ["python3", "${path.module}/get_mac_addr.py"]
}

output "external_data" {
  value = data.external.example.result
}



