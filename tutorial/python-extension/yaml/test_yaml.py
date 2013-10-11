import yaml
import os

ROOT_DIR = os.path.dirname(__file__)
print(__file__)
print(ROOT_DIR)

yaml_filename = 'settings.yml'
default_yaml_path = os.path.join(ROOT_DIR,yaml_filename)
print(default_yaml_path)

config = {}
yamlfile = 'settings.yml'
f = open(yamlfile,'r')
config = yaml.load(f)
print config
