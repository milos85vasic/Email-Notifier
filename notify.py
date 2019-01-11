import sys

from notify_api import *

message = ""
configuration_names = []

for arg in sys.argv:
    if sys.argv.index(arg) > 0:
        if param_configuration_names not in arg:
            message += arg + "\n"
        else:
            configuration_name = arg.replace(param_configuration_names, "")
            configuration_name = configuration_name.replace("=", "")
            configuration_name = configuration_name.replace("'", "")
            configuration_name = configuration_name.replace("\"", "")
            configuration_name = configuration_name.replace(" ", "")
            configuration_names.extend(configuration_name.split(","))

if __name__ == '__main__':
    if notify(message, configuration_names):
        log("Message sent.")
