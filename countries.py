import json

with open("countries.json") as f:
    data = json.load(f)

country = input("Enter Country:\n")

for c in data:
    if c['name'] == country:
        print(c["capital"])
