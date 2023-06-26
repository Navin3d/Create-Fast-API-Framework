import os
system_type = os.name
app_name = input("Enter Project Name: ")

if system_type == 'posix':
    os.system(f'git clone https://github.com/Navin3d/Fast-API-Framework.git {app_name}')
    os.chdir(f'{os.getcwd()}/{app_name}')
    os.system('python3 -m venv venv')
    os.system('source venv/bin/activate')
    os.system('pip3 install -r requirements.txt')
else:
    os.system(f'git clone https://github.com/Navin3d/Fast-API-Framework.git {app_name}')
    os.system(f'cd {app_name}')
    os.system('python -m venv venv')
    os.system('venv/scripts/activate')
    os.system('pip install -r requirements.txt')
