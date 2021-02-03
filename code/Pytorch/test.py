import json
import sys

with open(sys.argv[1]) as json_data:
    run_options = json.load(json_data)
    # for key, values in run_options.items():
    #     print(key, values)


