from studentworks import Student

# Object
newStudent = Student()
print(newStudent.students)

print("Student Registration")
while True:
    choice = int(input('''
1. Register Student
2. Issue WiFi
3. Enrol into Course
                   '''))
    
    if choice == 1:
        name = input("Enter Name:")
        id = int(input("Enter ID"))

        newStudent.save_student(name,id)
    



# 1. Register Student
# 2. Issue Wifi
# 3. Join Course

