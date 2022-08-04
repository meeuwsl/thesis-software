import json

conf_file = open("exp/json/config.json")
conf_data = json.load(conf_file)
#print(conf_data)
#print(type(conf_data))
#print(conf_data["end_devices"][0]["modules"][0]["topic"])

self_ip = "192.168.1.104"

end_device_count = len(conf_data["end_devices"])
print(end_device_count)

for i in range(end_device_count):
    if (conf_data["end_devices"][i]["ip"] == self_ip):
        conf_this_end_device = conf_data["end_devices"][i]


modules_count = len(conf_this_end_device["modules"])
print(modules_count)










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
