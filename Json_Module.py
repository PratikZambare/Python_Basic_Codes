import json

data = '{"var1":"pratik", "var2":"56"}'
# print(data)

parsed = json.loads(data)
print(parsed['var1'])

data2 = {
    "channel name " : "Code with harry",
    "cars" : "'bmw', 'audi', 'mercerdise' ",

}