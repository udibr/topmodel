import yaml

def read_config(filename):
    with open(filename) as f:
        config = yaml.load(f)
    if 'bucket' not in config.keys():
        raise Exception('Invalid config file: bucket is missing')
    return config
