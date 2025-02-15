from sys import version as sysdotversion, platform as sysdotplatform
from shutil import which
from subprocess import check_output
from os import system, path
try: from yaml import safe_load as yamlload, YAMLError
except ImportError: print("Install pyyaml from pip to use qtt"); exit(1)