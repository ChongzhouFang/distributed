import dask
import distributed
import os
import asyncio
import signal
import psutil

# command = 'export AZURE_FUNCTIONS_ENVIRONMENT=Development;\
#         export AzureWebJobsScriptRoot=/home/GCPkey/azure-functions-host/src/WebJobs.Script.WebHost/Resources/Functions/;\
#         dotnet run --project /home/GCPkey/azure-functions-host/src/WebJobs.Script.WebHost/WebJobs.Script.WebHost.csproj'

def exec(c):
        return os.system(c)

async def launch_function_host(function_name: str):
    # retrieve repo from github
#     os.system('wget https://github.com/ChongzhouFang/azure-functions-host/archive/refs/heads/' + function_name + '.zip')
#     os.system('unzip -qq ' + function_name + '.zip')
    host_folder = 'azure-functions-host-' + function_name + '/'
    current_folder = os.getcwd()
    try:
        process = await asyncio.create_subprocess_exec(
            'dotnet', 'run', '--project',
            os.path.join(current_folder, host_folder, 'src/WebJobs.Script.WebHost/WebJobs.Script.WebHost.csproj'),
            env={
                    'AZURE_FUNCTIONS_ENVIRONMENT': 'Development',
                    'AzureWebJobsScriptRoot': os.path.join(current_folder, host_folder, 'src/WebJobs.Script.WebHost/Resources/Functions/'),
                    'PATH': os.environ['PATH'],
                    'DOTNET_CLI_HOME': '/home/jiujiu'
                }
        )

        await asyncio.gather(process.wait(), asyncio.sleep(0))

    except asyncio.CancelledError:
        print("Function host was cancelled.")
        terminate_dotnet_processes(process.pid)


def terminate_dotnet_processes(main_pid):
    try:
        main_process = psutil.Process(main_pid)

        # Get all child processes of the main dotnet process
        children = main_process.children(recursive=True)

        # Terminate all child processes
        for child in children:
            child.terminate()

        # Wait for a short time to allow processes to terminate gracefully
        _, alive = psutil.wait_procs(children, timeout=1)

        # Terminate any remaining alive processes
        for child in alive:
            child.terminate()

        # Wait for another short time
        _, alive = psutil.wait_procs(alive, timeout=1)

        # Kill any remaining processes forcefully
        for child in alive:
            child.kill()

        # Terminate the main dotnet process
        main_process.terminate()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Handle exceptions as needed
        pass


async def main():
    task_handler = asyncio.create_task(launch_function_host('warmup'))
    await asyncio.sleep(120)
    print('Times up! Closing host.')
    task_handler.cancel()


async def test_command():
    res = await asyncio.create_subprocess_exec('curl', 'http://localhost:5000/api/warmup')
    print(res)

if __name__ == '__main__':
    # c = distributed.Client('tcp://192.168.1.111:8786')
    # futures = c.submit(exec, command)

    # asyncio.run(main())

    asyncio.run(test_command())
    
