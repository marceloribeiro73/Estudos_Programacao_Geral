terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.70.0"
    }
  }
}
provider "azurerm" {
  features {}

}

module "az_adds" {
  source = "./modules/adds"

  resource_group_name = azurerm_resource_group.az_rg_grp_01.name
  location = azurerm_resource_group.az_rg_grp_01.location
  active_directory_domain_name = join(".",[var.ad_domainName,"local"])
  active_directory_netbios_name = var.ad_domainName
  admin_username                = var.az_vm01_ad01_admin_user
  admin_password                = var.az_vm01_ad01_admin_pwd
  prefix                        = "lab-AwON"
  subnet_id = azurerm_subnet.az_vnet-01_subnet-01.id
}

resource "azurerm_resource_group" "az_rg_grp_01" {
  name     = var.az_rg_name
  location = var.az_rg_1_region
  tags     = var.az_tags
}

resource "azurerm_virtual_network" "az_vnet-01" {
  name                = var.az_vnet_name_01
  location            = azurerm_resource_group.az_rg_grp_01.location
  resource_group_name = azurerm_resource_group.az_rg_grp_01.name
  address_space       = ["10.0.0.0/16"]

}

resource "azurerm_subnet" "az_vnet-01_subnet-01" {
  name                 = join("_", [var.az_vnet_name_01, "subnet-01"])
  resource_group_name  = azurerm_resource_group.az_rg_grp_01.name
  virtual_network_name = azurerm_virtual_network.az_vnet-01.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_virtual_network" "az_vnet-02" {
  name                = var.az_vnet_name_02
  location            = var.az_vnet-02_location
  resource_group_name = azurerm_resource_group.az_rg_grp_01.name
  address_space       = ["10.1.0.0/16"]

}

resource "azurerm_subnet" "az_vnet-02_subnet-01" {
  name                 = join("_", [var.az_vnet_name_02, "subnet-01"])
  resource_group_name  = azurerm_resource_group.az_rg_grp_01.name
  virtual_network_name = azurerm_virtual_network.az_vnet-02.name
  address_prefixes     = ["10.1.1.0/24"]
}

#NSGs
resource "azurerm_network_security_group" "az_nsg-01" {
  name                = local.az_nsg01_name
  location            = local.az_rg01_location
  resource_group_name = local.az_rg01_name
  tags                = var.az_tags

}

resource "azurerm_subnet_network_security_group_association" "az_nsg01_vnet01-subnet01" {
  subnet_id                 = azurerm_subnet.az_vnet-01_subnet-01.id
  network_security_group_id = azurerm_network_security_group.az_nsg-01.id
}

resource "azurerm_network_security_rule" "az_nsg-01_rule-01" {
  name                        = "ConectFromIpRDP"
  priority                    = 200
  direction                   = "Inbound"
  access                      = "Allow"
  source_port_range           = "*"
  destination_port_range      = "3389"
  protocol                    = "Tcp"
  source_address_prefix       = var.az_source_ip_nsg01_rule01
  destination_address_prefix  = element(azurerm_subnet.az_vnet-01_subnet-01.address_prefixes, 0)
  description                 = "Rule for conection to vms on subnet01 of vnet 01 using rdp"
  network_security_group_name = azurerm_network_security_group.az_nsg-01.name
  resource_group_name         = local.az_rg01_name
}

#VM for AD
resource "azurerm_network_interface" "az_nic01_vm01-ad01" {
  name                = join("-", [var.az_vnet_name_01, "nic01_vm01-ad01"])
  location            = azurerm_resource_group.az_rg_grp_01.location
  resource_group_name = azurerm_resource_group.az_rg_grp_01.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.az_vnet-01_subnet-01.id
    private_ip_address_allocation = "Static"
    private_ip_address            = "10.0.1.5"
    public_ip_address_id          = azurerm_public_ip.az_pip01_vm01.id
  }
}


resource "azurerm_public_ip" "az_pip01_vm01" {
  name                = join("-", [local.az_vm01_name, "pip01"])
  resource_group_name = azurerm_resource_group.az_rg_grp_01.name
  location            = azurerm_resource_group.az_rg_grp_01.location
  allocation_method   = "Static"
  tags                = var.az_tags
}


# resource "azurerm_windows_virtual_machine" "az_vm01_ad01" {
#   name                  = local.az_vm01_name
#   resource_group_name   = azurerm_resource_group.az_rg_grp_01.name
#   location              = azurerm_resource_group.az_rg_grp_01.location
#   size                  = "Standard_B1ms"
#   admin_username        = var.az_vm01_ad01_admin_user
#   admin_password        = var.az_vm01_ad01_admin_pwd
#   network_interface_ids = [azurerm_network_interface.az_nic01_vm01-ad01.id]


#   os_disk {
#     name                 = "vm01_dsk01"
#     caching              = "ReadWrite"
#     storage_account_type = "Standard_LRS"
#   }
#   source_image_reference {
#     publisher = "MicrosoftWindowsServer"
#     offer     = "WindowsServer"
#     sku       = "2019-Datacenter"
#     version   = "latest"
#   }
# }
# resource "azurerm_virtual_machine_extension" "wait-for-domain-to-provision" {
#   name                 = "TestConnectionDomain"
#   publisher            = "Microsoft.Compute"
#   type                 = "CustomScriptExtension"
#   type_handler_version = "1.9"
#   virtual_machine_id   = azurerm_windows_virtual_machine.az_vm01_ad01.id
#   settings             = <<SETTINGS
#   {
#     "commandToExecute": "powershell.exe -Command \"while (!(Test-Connection -ComputerName ${join(".",[local.ad_domainName,"local"])} -Count 1 -Quiet) -and ($retryCount++ -le 360)) { Start-Sleep 10 } \""
#   }
# SETTINGS
# }

