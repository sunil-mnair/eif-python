import json

# Add to the File
# Step 1 - Read from the File
with open("customer.json") as f:
    data = json.load(f)

# Step 2 - Update and Dump into the File
print("Registration")
name = input("Enter Name:")
age = int(input("Enter Age:"))
membership = input("Membership Type")

## Add to the List
data.append({'Name':name,'Age':age,'Membership':membership})
print(data)

# Dump the List to JSON
with open("customer.json","w") as f:
    json.dump(data,f,indent=2)