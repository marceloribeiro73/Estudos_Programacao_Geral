//Aula 25 - Variables

@minLength(3)
@maxLength(24)
@description('Name do StorageAccount')
param storageAccountName string 

@description('Regiao onde o StorageAccount vai ser criado')
param storageAccountLocation string = 'eastus2'

@allowed(['Standard_LRS', 'Standard_GRS'])
@description('Sku do StorageAccount')
param storageAccountSku string = 'Standard_LRS'

var minTlsVersion  = 'TLS1_2'

var httpsTrafic = true

var storageAccountKind = 'StorageV2'

targetScope = 'resourceGroup'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: storageAccountLocation
  sku: {
    name: storageAccountSku
  }
  kind: storageAccountKind
  properties:{
    minimumTlsVersion: minTlsVersion
    supportsHttpsTrafficOnly: httpsTrafic
  }
}
