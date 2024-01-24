
targetScope = 'resourceGroup'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'strdevbicepcourse'
  location: 'eastus2'
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
