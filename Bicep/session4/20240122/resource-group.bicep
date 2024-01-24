targetScope = 'subscription'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2023-07-01' = {
  name: 'rg-dev-bicepCourse'
  location: 'eastus'
}
