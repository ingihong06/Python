import json

x = (1, 2, 3)
y = json.dumps(x)
print(y)
print(type(y))

x = json.loads(y)
print(x)
print(type(x))

x = '{ "name":"SWH", "age":3, "subject":"Coding" }'
y = json.loads(x)

print(x)
print(type(x))
print(y)
print(type(y))
print(y["name"])  # 딕셔너리 타입
# print(x["age"])    # ?
x = {"name": "SWH", "age": 3, "subject": "Coding"}
y = json.dumps(x)

asdf = {"아이디" : "메세지"}
afsd = json.dumps(asdf)
fasd = json.loads(afsd)