resource "azurerm_windows_virtual_machine" "vm_domain_joined_vm" {
  name = var.vm_name
  resource_group_name = var.resource_group_name
  location = var.location
  size = var.vm_size
  admin_password = var.ad_admin_pwsd
  admin_username = var.ad_admin_name
  provision_vm_agent = true
  enable_automatic_updates = true
  
  network_interface_ids = [ azurerm_network_interface.vms_primary_nic.id ]

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer =   "WindowsServer"
    sku       = "2016-Datacenter"
    version   = "latest"
  }

  os_disk {
    caching = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
}

resource "azurerm_network_interface" "vms_primary_nic" {
  name = join("-", [var.vm_name, "nic"])
  location = var.location
  resource_group_name = var.resource_group_name
  ip_configuration {
    name = "primary-nic"
    subnet_id = var.subnet
    private_ip_address_allocation = "Static"
    private_ip_address = var.vm_ip_address
    public_ip_address_id = azurerm_public_ip.vm_public_ip.id
  }
}

resource "azurerm_public_ip" "vm_public_ip" {
    name = join("-",["pip",var.vm_name])
    location = var.location
    resource_group_name = var.resource_group_name
    allocation_method = "Static"
  
}

resource "azurerm_virtual_machine_extension" "wait_ad_prov" {
  name = "TestIfAdIsUp"
  publisher            = "Microsoft.Compute"
  type                 = "CustomScriptExtension"
  type_handler_version = "1.9"
  virtual_machine_id = azurerm_windows_virtual_machine.vm_domain_joined_vm.id
  settings             = <<SETTINGS
  {
    "commandToExecute": "powershell.exe -Command \"while (!(Test-Connection -ComputerName ${var.ad_name} -Count 1 -Quiet) -and ($retryCount++ -le 360)) { Start-Sleep 10 } \""
  }
SETTINGS

}

resource "azurerm_virtual_machine_extension" "join_vm_ad" {
  name = join("-",[azurerm_windows_virtual_machine.vm_domain_joined_vm.name, "exten-join-ad"])
  publisher            = "Microsoft.Compute"
  type                 = "JsonADDomainExtension"
  type_handler_version = "1.3"
  virtual_machine_id = azurerm_windows_virtual_machine.vm_domain_joined_vm.id

  settings = <<SETTINGS
    {
        "Name": "${var.ad_name}",
        "OUPath": "",
        "User": "${var.ad_admin_name}@${var.ad_name}",
        "Restart": "true",
        "Options": "3"
    }
SETTINGS

  protected_settings = <<SETTINGS
    {
        "Password": "${var.ad_admin_pwsd}"
    }
SETTINGS

    depends_on = [ azurerm_virtual_machine_extension.wait_ad_prov ]
}