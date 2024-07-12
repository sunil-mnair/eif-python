import json

# Read Data - load() method
with open("customer.json") as f:
    data = json.load(f)
    
for customer in data:
    if customer["Age"] >= 30:
        print(customer)

# Setup up a Query
name = input("Enter Name:")

for customer in data:
    if customer['Name'] == name:
        print(f'''
Name:       {customer["Name"]}
Age:        {customer["Age"]}
Membership: {customer["Membership"]}
''')


# Write Data - dump() method