para1 = '''This is a sample para
This is line 2
This is line 3'''

#print(para1)

name = input("Name: ")
course = input("Course: ")
age = int(input("Age: "))

email_template = f'''Dear {name},
Thank you for joining the course on {course}
Thank You'''

print(email_template)