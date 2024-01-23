#inputs
variable "vm_name" {
  
}

variable "location" {
  
}

variable "resource_group_name" {
  
}

variable "subnet" {
  
}

variable "ad_name" {
  
}

variable "ad_admin_name" {
  
}

variable "ad_admin_pwsd" {
  
}

variable "vm_size" {
  
}

variable "vm_ip_address" {
  
}

#locals

locals {
   wait_for_domain_command = "while (!(Test-Connection -TargetName ${var.ad_name} -Count 1 -Quiet) -and ($retryCount++ -le 360)) { Start-Sleep 10 }"
}