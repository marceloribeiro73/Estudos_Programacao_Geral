#Inputs

variable "az_rg_name" {

}

variable "az_rg_1_region" {

}

variable "az_tags" {
  type = map(any)
}

variable "az_vnet_name_01" {

}

variable "az_vnet_name_02" {

}

variable "az_vnet-02_location" {

}

variable "az_vm01_ad01_admin_user" {

}

variable "az_vm01_ad01_admin_pwd" {

}

variable "ad_domainName" {

}
variable "az_source_ip_nsg01_rule01" {

}

#Outpus

output "az_pip01_vm01_ip" {
  depends_on  = [azurerm_public_ip.az_pip01_vm01]
  value       = azurerm_public_ip.az_pip01_vm01.ip_address
  description = "Public ip addr for vm01"
}


#locals

locals {
  az_nsg01_name           = join("_", [lookup(var.az_tags, "enviroment", "teste"), lookup(var.az_tags, "project", "lab"), "nsg01"])
  az_rg01_name            = azurerm_resource_group.az_rg_grp_01.name
  az_rg01_location        = azurerm_resource_group.az_rg_grp_01.location
  az_vm01_name            = "vm01-ad01"
  }

