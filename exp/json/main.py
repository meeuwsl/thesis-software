import json

conf_file = open("exp/json/config.json")
conf_data = json.load(conf_file)
#print(conf_data)
#print(type(conf_data))
print(conf_data["end_devices"][1])















# data = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# print("data: ", data)
# print("name = ", data.get("name"))

# data_out = json.dumps(data)
# print("data out: ", data_out)
# print("type of data_out: ", type(data_out))


# data_in = json.loads(data_out)
# print("data in: ", data_in)
# print("name = ", data_in.get("name"))
# print("type of data_in: ", type(data_in))
