#fazendo o depoy para um resource group
az deployment group create \
    --resource-group rg-course-bicep-udemy \
    --template-file main.bicep \
    --name azureCliDeployment \
    --subscription 'Ass. do Visual Studio Enterprise Marcelo Silva - Dataex' \
    --what-if