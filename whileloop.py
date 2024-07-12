import random
x=0

while x != 3:
    x = random.randint(1,5)
    print(x)

# Infinite Loop
while True:
    choice = input("Press e to exit")
    if choice == "e":
        break

