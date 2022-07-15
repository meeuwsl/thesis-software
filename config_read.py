import json

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
#print(data)

print(data["end1"]["ip"])