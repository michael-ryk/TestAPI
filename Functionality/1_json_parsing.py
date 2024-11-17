import json

response = '{"answer":"Hello, User"}'
obj_json = json.loads(response)

print(obj_json["answer"])           # May raise exception if key doesn't exist
print(obj_json.get("unexist"))      # print Null if key doesn't exists