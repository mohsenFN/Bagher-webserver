import os

def init():
    cwd = os.getcwd()
    storage_path = cwd+'/storage'
    # make directory if not exists
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)
    return 'storage', storage_path


# Usage example --> custom_storage_dir('/tmp/project', 'storage')
def custom_storage_dir(address, dir_name):
    return dir_name, address+dir_name