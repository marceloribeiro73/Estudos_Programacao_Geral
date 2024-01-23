

resource storageAccount1 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'stdevbicepcourse'
  location: 'eastus'
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
