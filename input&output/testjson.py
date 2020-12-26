import json
data={
    "name":["jerry","nickname"],
    "age":26,
    "gender":"female"
}

data1=json.dumps(data)

print(type(data))
print(data1)
print(type(data1))

data2=json.loads(data1)
print(type(data2))
