targetScope = 'subscription'

param param_env_id string

param param_location string

resource rgTeste 'Microsoft.Resources/resourceGroups@2024-07-01' = {
  name: 'rg-br-${param_env_id}-teste'
  location: param_location
}

module networking 'modules/networking.bicep' = {
  scope: rgTeste
  name: 'networking-depoyment'
  params: {
    env_id: param_env_id
  }
}
