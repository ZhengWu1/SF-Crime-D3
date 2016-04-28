import json
from sets import Set

keys = Set()

f = open("scpd_incidents.json", "r")
j = json.load(f)
f.close()
for i in j["data"]:
	keys.add(i["Resolution"])

for key in keys:
	print key

