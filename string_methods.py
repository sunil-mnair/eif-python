name = " Sunil Nair  "

print(name.strip()) # Sunil Nair
print(name.upper()) # SUNIL NAIR

print(name.strip().upper()) #SUNIL NAIR

fullname = "Sunil Nair"
print(fullname.split()) # ['Sunil','Nair']
firstname,lastname = fullname.split()
print(firstname)
print(lastname)

new_fullname = "-".join(['Sunil','Nair'])
print(new_fullname)