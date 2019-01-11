import sys

from notify_api import *

configuration_names = []

for arg in sys.argv:
    if sys.argv.index(arg) > 0 and param_configuration_names in arg:
        configuration_name = arg.replace(param_configuration_names, "")
        configuration_name = configuration_name.replace("=", "")
        configuration_name = configuration_name.replace("'", "")
        configuration_name = configuration_name.replace("\"", "")
        configuration_name = configuration_name.replace(" ", "")
        configuration_names = configuration_name.split(",")

message = ""

for line in sys.stdin:
    message += line + "\n"

notify(message, configuration_names)
