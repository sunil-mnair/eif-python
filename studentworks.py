import json
# Student Registration

class Student:
    def __init__(self,name=None,id=None):
        self.name = name
        self.id = id

    def save_student(self,name,id):
        self.name = name
        self.id = id
        # Read Existing Student File
        with open("student.json") as f:
            students = json.load(f)
        
        students.append({"name":self.name,"id":self.id})
        
        # Write to File
        with open("student.json","w") as f:
            json.dump(students,f,indent=2)
        
        print(f"{self.name} successfully registered")

    
    # Get WiFi
    def issue_wifi(self):
        print(f'Wifi Issed to {self.name}')

    def join_course(self,course):
        print(f'{self.name} has joined {course}')


# hassan = Student(name="Hassan Ahmed",id=3045)
# print(hassan.name)
# hassan.issue_wifi()
# hassan.join_course(course="Python Programming")