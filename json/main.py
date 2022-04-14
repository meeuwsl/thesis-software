import json



data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print("data: ", data)
print("name = ", data.get("name"))

data_out = json.dumps(data)
print("data out: ", data_out)
print("type of data_out: ", type(data_out))


data_in = json.loads(data_out)
print("data in: ", data_in)
print("name = ", data_in.get("name"))
print("type of data_in: ", type(data_in))
