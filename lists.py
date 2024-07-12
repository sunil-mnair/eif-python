loan_purpose = ['House', 'Education', 'Medical',
                 'Vacation', 'Wedding', 'Others']
# List is Mutable
print(type(loan_purpose))

# Printing the List
print(loan_purpose)

x = 1
for purpose in loan_purpose:
    print(x,purpose)
    x += 1

for x,purpose in enumerate(loan_purpose,1):
    print(x,purpose)


# Add to the List - Option 1
loan_purpose.append("Car")
print(loan_purpose)

# Add to the List - Option 2
loan_purpose.insert(0,"Home Improvement")
print(loan_purpose)

# Update the List
loan_purpose[0] = "Home Repairs"
print(loan_purpose)

# Remove the List Item- Option 1
loan_purpose.remove("Car")
print(loan_purpose)

# Remove the List Item - Option 2
loan_purpose.pop(0)
print(loan_purpose)

loan_purpose = ('House', 'Education', 'Medical',
                 'Vacation', 'Wedding', 'Others')

loan_purpose = list(loan_purpose)

# Tuple is read-only
print(type(loan_purpose))