#!/usr/bin/env python3
import json
with open("states.json") as f:
	file = f.read()

file = json.loads(file,  )
print(type(file))
file = json.dumps(file, indent=2, sort_keys=True)
print(file)
print(type(file))

print("#" * 40)


