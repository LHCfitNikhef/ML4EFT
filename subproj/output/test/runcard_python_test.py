import json

with open("test_runcard.json", "r") as json_runcard:
    json_runcard_loaded = json.load(json_runcard)

name = json_runcard_loaded["name"]


print(name)