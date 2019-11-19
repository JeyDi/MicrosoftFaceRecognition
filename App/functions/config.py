import yaml
import os

def define_path(folder=None):
    """
    Define Project folder
    """
    folder_path = os.path.abspath('')

    if(folder is not None):
        folder_path = os.path.join(folder_path,folder)

    return folder_path

def read_yaml_config(PATH,filename='config.yml'):
    """
    Read a YAML Config file with your azure key
    """
    file_path = os.path.join(PATH,filename)
    with open(file_path, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    SUB_KEY = cfg['SUBSCRIPTION_KEY']
    ENDPOINT = cfg['ENDPOINT']
    
    return SUB_KEY, ENDPOINT