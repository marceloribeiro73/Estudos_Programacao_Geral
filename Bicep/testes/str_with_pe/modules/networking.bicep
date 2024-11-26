param env_id string
param location string = resourceGroup().location
param nsg_securityRules array = []

resource vnet 'Microsoft.Network/virtualNetworks@2024-03-01' = {
  name: 'vnet-br-${env_id}-teste'
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        '10.0.0.0/16'
      ]
    }
    subnets: [
      {
        name: 'default'
        properties: {
          addressPrefix: '10.0.0.0/24'
          networkSecurityGroup: {
            id : nsg.id
          }
        }
      }
      {
        name: 'subnet-br-${env_id}-teste-01'
        properties: {
          addressPrefix: '10.0.1.0/24'
          networkSecurityGroup: {
            id: nsg.id
          }
        }
      }
    ]
  }
}

resource nsg 'Microsoft.Network/networkSecurityGroups@2024-03-01' = {
  name: 'nsg-br-${env_id}-teste'
  location: location
  properties: {
    securityRules: [for rule in nsg_securityRules: {
      name: rule.name
      properties: rule.properties
    }]
  }
}

output out_obj_vnet object = vnet
