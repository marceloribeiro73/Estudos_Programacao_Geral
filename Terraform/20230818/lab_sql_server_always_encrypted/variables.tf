
variable "azMssqlServerName" {
  
}
variable "azResourceGroupName" {
  
}
variable "azResourceGroupRegion" {
  
}
variable "azMssqlServerAdminName" {
  sensitive = true
}
variable "azMssqlServerAdminPasswd" {
  sensitive = true
}
variable "azTags" {
  type = map()
  default = {
    env = "lab",
    project = "mssqlAE"
  }
}