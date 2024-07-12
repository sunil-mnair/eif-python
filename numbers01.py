number1 = int(input("Enter a Number of your choice:\n"))
number2 = int(input("Enter a Second Number :\n"))

# The below code multiplies the '-' dash character 30 times
print('-' * 30)

sum_value = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = round(number1 / number2, 2)
modulus = number1 % number2
exponent = number1 ** number2

print(f'''The sum of the numbers is {sum_value}
The difference of the numbers is {difference}
The product of the numbers is {product} 
The quotient of the numbers is {quotient}
The remainder/modulus of the numbers is {modulus}
{number1} raised to the power of {number2} is {exponent}
''')