import json
import os

def add_student():
    
    new_student = {
        "Name": input("Enter Student Name: "),
        "FatherName": input("Enter Student's Father Name: "),
        "FatherContact": input("Enter Student's Father Contact Number: "),
        "Age": input("Enter Student Age: "),
        "RollNo": input("Enter Student Roll Number: "),
        "Class": input("Enter Student Class: "),
        "Address": input("Enter Student Address: ")
    }
    
    if os.path.exists("Data/Student.json"):
        with open("Data/Student.json", "r") as file:
            students = json.load(file)
    else:
        students = []
        
    
    students.append(new_student)
    
    with open("Data/Student.json", "w") as file:
        json.dump(students, file, indent=4)
        
    print("\n** Student added successfully!\n")


def view_all_students():
    
    if not os.path.exists("Data/Student.json"):
        print("\n** No student data found. File does not exist.\n")
        return
    
    
    with open("Data/Student.json", "r") as file:
        students = json.load(file)
        
    
    if len(students) == 0:
        print("\n** No students found.\n")
        return
    
    
    print("\n----> All Students <----\n")
    
    for index, student in enumerate(students, start = 1):
        print(f"- Student {index}: ")
        print(f"\tName: {student["Name"]}")
        print(f"\tFather Name: {student['FatherName']}")
        print(f"\tFather Contact: {student['FatherContact']}")
        print(f"\tAge: {student['Age']}")
        print(f"\tRoll No: {student['RollNo']}")
        print(f"\tClass: {student['Class']}")
        print(f"\tAddress: {student['Address']}")
        print("----------------------------------------")
        
        
        
def delete_a_student():
    
    if not os.path.exists("Data/Student.json"):
        print("\n** No student data found. File does not exist.\n")
        return
    
    with open("Data/Student.json", "r") as file:
        students = json.load(file)
        
    
    if len(students) == 0:
        print("\n** No students found.\n")
        return
    
    condition1 = True
    
    
    while condition1:
    
        roll_no_to_delete = input("Enter the Roll Number of student to delete data: ")
    
        for student in students:
            
            if student["RollNo"] == roll_no_to_delete:
                
                print("\n- Student Found:\n")
                print(f"\tName: {student["Name"]}")
                print(f"\tFather Name: {student['FatherName']}")
                print(f"\tFather Contact: {student['FatherContact']}")
                print(f"\tAge: {student['Age']}")
                print(f"\tRoll No: {student['RollNo']}")
                print(f"\tClass: {student['Class']}")
                print(f"\tAddress: {student['Address']}\n")
                
                choice3 = input("Do you want to delete data? (y/n): ").lower()
                
                if choice3 == "y":
                    
                    students.remove(student)
                
                    with open("Data/Student.json", "w") as file:
                        json.dump(students, file, indent=4)
                    print("\n** Student data deleted successfully!\n")
                    condition1 = False
                    return
                
                
                else:
                    print("\nDeletion Cancelled!\n")
                    condition1 = False
                    
                    
            else:
                print("\n** No student with such credentials found!\n")
            
        
        
        
def search_specific_student():
    
    if not os.path.exists("Data/Student.json"):
        print("\n** No student data found. File does not exist.\n")
        return
    
    with open("Data/Student.json", "r") as file:
        students = json.load(file)
        
    
    if len(students) == 0:
        print("\n** No students found.\n")
        return
    
    condition2 = True
    
    while condition2:
    
        roll_no_to_search = input("Enter the Roll Number of student to search data: ")
        
        for student in students:
            
            if student["RollNo"] == roll_no_to_search:
                print("\n- Student Found:\n")
                print(f"\tName: {student["Name"]}")
                print(f"\tFather Name: {student['FatherName']}")
                print(f"\tFather Contact: {student['FatherContact']}")
                print(f"\tAge: {student['Age']}")
                print(f"\tRoll No: {student['RollNo']}")
                print(f"\tClass: {student['Class']}")
                print(f"\tAddress: {student['Address']}\n")
                
                condition2 = False
                
            else:
                print("\n** No student with such credentials found!\n")
            
            
            
def update_student_data():
    
    if not os.path.exists("Data/Student.json"):
        print("\n** No student data found. File does not exist.\n")
        return
    
    with open("Data/Student.json", "r") as file:
        students = json.load(file)
        
    
    if len(students) == 0:
        print("\n** No students found.\n")
        return
    
    condition3 = True
    
    while condition3:
    
        roll_no_to_update = input("Enter the Roll Number of student to update data: ")
    
        for student in students: 
            
            if student["RollNo"] == roll_no_to_update:
                
                print("\n- Student Found:\n")
                print(f"\tName: {student["Name"]}")
                print(f"\tFather Name: {student['FatherName']}")
                print(f"\tFather Contact: {student['FatherContact']}")
                print(f"\tAge: {student['Age']}")
                print(f"\tRoll No: {student['RollNo']}")
                print(f"\tClass: {student['Class']}")
                print(f"\tAddress: {student['Address']}\n")
                
                print("\nEnter new data (Leave blank to keep current data):\n")
                
                Name = input("Enter Student Name: ")
                Father_Name = input("Enter Student's Father Name: ")
                Father_Contact = input("Enter Student's Father Contact Number: ")
                Age = input("Enter Student Age: ")
                Roll_No = input("Enter Student Roll Number: ")
                Class = input("Enter Student Class: ")
                Address = input("Enter Student Address: ")
            
                student.update({
                    "Name": Name if Name else student["Name"],
                    "FatherName": Father_Name if Father_Name else student["FatherName"],
                    "FatherContact": Father_Contact if Father_Contact else student["FatherContact"],
                    "Age": Age if Age else student["Age"],
                    "RollNo": Roll_No if Roll_No else student["RollNo"],
                    "Class": Class if Class else student["Class"],
                    "Address": Address if Address else student["Address"]
                })
            
                print("\nStudent data updated successfully!\n")
                
                print(f"\tName: {student["Name"]}")
                print(f"\tFather Name: {student['FatherName']}")
                print(f"\tFather Contact: {student['FatherContact']}")
                print(f"\tAge: {student['Age']}")
                print(f"\tRoll No: {student['RollNo']}")
                print(f"\tClass: {student['Class']}")
                print(f"\tAddress: {student['Address']}\n")
                
                with open("Data/Student.json", "w") as file:
                    json.dump(students, file, indent=4)
                    
                condition3 = False
                
            else:
                print("\n** No student with such credentials found!\n")
            
            
           

def enter_student_portal():
    
    if not os.path.exists("Data/Student.json"):
        print("\n** No student data found. File does not exist.\n")
        return
    
    with open("Data/Student.json", "r") as file:
        students = json.load(file)
        
    
    if len(students) == 0:
        print("\n** No students found.\n")
        return
    
    condition4 = True
    
    while condition4:
    
        username = input("Enter Student Name: ")
        password = input("Enter Roll Number: ")
        
        for student in students:
            
            if student["Name"] == username and student["RollNo"] == password:
                print("\nLogin successful!\n")
                print(f"\nWelcome to the Student Portal, {username}!\n")
                
                print(f"\tName: {student["Name"]}")
                print(f"\tFather Name: {student['FatherName']}")
                print(f"\tFather Contact: {student['FatherContact']}")
                print(f"\tAge: {student['Age']}")
                print(f"\tRoll No: {student['RollNo']}")
                print(f"\tClass: {student['Class']}")
                print(f"\tAddress: {student['Address']}\n")
                
                condition4 = False
                
            else:
                print("\nInvalid credentials. Please try again.")
        
        
    
     