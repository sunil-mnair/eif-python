

print(type(customer))

# Printing the Dict
print(customer)

# Printing the Keys
for key in customer:
    print(key)
# Printing the Keys and Values
for key,value in customer.items():
    print(key,value)
# Printing the Values
for value in customer.values():
    print(value)

# Update
customer['Name']="John Doe"
print(customer)

# Add
customer['Type']="A"
print(customer)

# Remove
customer.pop("Type")
print(customer)
