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

resource "azurerm_mssql_server" "az_mssqlSrv01" {
  name = var.azMssqlServerName
  resource_group_name = azurerm_resource_group.az_rgLab.name
  location = azurerm_resource_group.az_rgLab.location
  version = "12.0"
  administrator_login = var.azMssqlServerAdminName
  administrator_login_password = var.azMssqlServerAdminPasswd
  minimum_tls_version = "1.2"
  tags = var.azTags
}

resource "azurerm_resource_group" "az_rgLab" {
  name = var.azResourceGroupName
  location = var.azResourceGroupRegion
  tags = var.azTags
}

resource "azurerm_mssql_firewall_rule" "az_fwMssqlServerRule01" {
  name = "inboudHomeIP"
  server_id =  azurerm_mssql_server.az_mssqlSrv01.id
  start_ip_address = var.azHomeIP
  end_ip_address = var.azHomeIP
}