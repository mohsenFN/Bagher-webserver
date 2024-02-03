import os

def make_storage_dir():
    cwd = os.getcwd()
    storage_path = cwd+'/storage'
    # make directory if not exists
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)