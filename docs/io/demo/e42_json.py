import json

data = {1:11, 2:22}
s = json.dumps(data)
data2 = json.loads(s)
