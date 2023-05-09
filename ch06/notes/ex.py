import json

data = {
    "num":1,
    "msg":"Hello World"
}

json_string = json.dumps(data)
print (json_string, type(json_string))

json_data = json.loads(json_string)

for k,v in json_data.items():
    print(k,v) #key, value

fptr = open("assets/data.json", "w") #json is a convention, its not a file type
fptr.write(json_string)
fptr.close()

data_str = open("assets/data.json")
data = json.loads(data_str)
print(data, type(data))
