terraform {
  required_providers {
    azurerm = {
        source = "hashicorp/azurerm"
        version = "3.70.0"
    }
  }
}
provider "azurerm" {
  features {}
  
}

resource "azurerm_resource_group" "az_rg_grp_01" {
  name = var.az_rg_name
  location = var.az_rg_1_region
  tags = var.az_tags
}