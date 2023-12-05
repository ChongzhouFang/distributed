import dask, distributed,os

# command = 'export AZURE_FUNCTIONS_ENVIRONMENT=Development;\
#         export AzureWebJobsScriptRoot=/home/GCPkey/azure-functions-host/src/WebJobs.Script.WebHost/Resources/Functions/;\
#         dotnet run --project /home/GCPkey/azure-functions-host/src/WebJobs.Script.WebHost/WebJobs.Script.WebHost.csproj'
command = 'ls -al'

def exec(c):
        return os.system(c)

c = distributed.Client('tcp://192.168.1.111:8786')
futures = c.submit(exec, command)