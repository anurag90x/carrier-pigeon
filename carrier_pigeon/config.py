from ConfigParser import ConfigParser

def read_config(config_file='./development.ini'):
    config = ConfigParser()
    config.read(config_file)
    conf = {}

    for section in config.sections():
        conf[section] = dict(config.items(section))
    return conf
