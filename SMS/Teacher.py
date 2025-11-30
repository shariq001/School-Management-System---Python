import json
import os

def add_teacher():
    
    new_teacher = {
        "Name": input("Enter Teacher Name: "),
        "Subject": input("Enter Teacher Subject: "),
        "Qualification": input("Enter Teacher Qualification: "),
        "Contact": input("Enter Teacher's Contact Number: "),
        "IdNo": input("Enter Teacher Id Number: "),
        "Email": input("Enter Teacher Email: ")
    } 
    
    if os.path.exists("Data/Teacher.json"):
        with open("Data/Teacher.json", "r") as file:
            teachers = json.load(file)
    else:
        teachers = []

    
    teachers.append(new_teacher)
    
    with open("Data/Teacher.json", "w") as file:
        json.dump(teachers, file, indent=4)
        
    print("\n** Teacher added successfully!\n")


def view_all_teachers():
    
    if not os.path.exists("Data/Teacher.json"):
        print("\n** No teacher data found. File does not exist.\n")
        return
    
    
    with open("Data/Teacher.json", "r") as file:
        teachers = json.load(file)
        
    
    if len(teachers) == 0:
        print("\n** No teachers found.\n")
        return
    
    
    print("\n\t----> All Teachers <----\n\t")
    
    for index, teacher in enumerate(teachers, start = 1):
        print(f"- Teacher {index}: ")
        print(f"\tName: {teacher["Name"]}")
        print(f"\tSubject: {teacher['Subject']}")
        print(f"\tQualification: {teacher['Qualification']}")
        print(f"\tContact: {teacher['Contact']}")
        print(f"\tId No: {teacher['IdNo']}")
        print(f"\tEmail: {teacher['Email']}")
        print("------------------------------")
        
        
        
def delete_a_teacher():
    
    if not os.path.exists("Data/Teacher.json"):
        print("\n** No teacher data found. File does not exist.\n")
        return
    
    with open("Data/Teacher.json", "r") as file:
        teachers = json.load(file)
        
    
    if len(teachers) == 0:
        print("\n** No teachers found.\n")
        return
    
    while True:
    
        id_no_to_delete = input("Enter the Id Number of teacher to delete data: ")
        
        found = False
        
        for teacher in teachers:
            
            if teacher["IdNo"] == id_no_to_delete:
                
                print("\n- Teacher Found:\n")
                print(f"\tName: {teacher["Name"]}")
                print(f"\tSubject: {teacher['Subject']}")
                print(f"\tQualification: {teacher['Qualification']}")
                print(f"\tContact: {teacher['Contact']}")
                print(f"\tId No: {teacher['IdNo']}")
                print(f"\tEmail: {teacher['Email']}\n")
                
                choice3 = input("Do you want to delete data? (y/n): ").lower()
                
                if choice3 == "y":
                     
                    teachers.remove(teacher)
                
                    with open("Data/Teacher.json", "w") as file:
                        json.dump(teachers, file, indent=4)
                    print("\n** Teacher data deleted successfully!\n")
                    return
                
                else:
                    print("\nDeletion Cancelled!\n")
                    return
                
                found = True
                break
                    
        if not found:
            print("\n** No teacher with such credentials found!\n")
        
        
        
def search_specific_teacher():
    
    if not os.path.exists("Data/Teacher.json"):
        print("\n** No teacher data found. File does not exist.\n")
        return
    
    with open("Data/Teacher.json", "r") as file:
        teachers = json.load(file)
        
    
    if len(teachers) == 0:
        print("\n** No teachers found.\n")
        return
    
    
    while True:
    
        id_no_to_search = input("Enter the Id Number of teacher to search data: ")
        
        found = False
        
        for teacher in teachers:
            
            if teacher["IdNo"] == id_no_to_search:
                print("\n- Teacher Found:\n")
                print(f"\tName: {teacher["Name"]}")
                print(f"\tSubject: {teacher['Subject']}")
                print(f"\tQualification: {teacher['Qualification']}")
                print(f"\tContact: {teacher['Contact']}")
                print(f"\tId No: {teacher['IdNo']}")
                print(f"\tEmail: {teacher['Email']}\n")
                
                found = True
                break
            
        if found:
            break
                
        else:
            print("\n** No teacher with such credentials found!\n")
            
            
            
            
            
def update_teacher_data():
    
    if not os.path.exists("Data/Teacher.json"):
        print("\n** No teacher data found. File does not exist.\n")
        return
    
    with open("Data/Teacher.json", "r") as file:
        teachers = json.load(file)
        
    
    if len(teachers) == 0:
        print("\n** No teachers found.\n")
        return
    
    
    
    while True:
    
        id_no_to_update = input("Enter the Id Number of teacher to update data: ")
        
        found = False
        
        for teacher in teachers: 
            
            if teacher["IdNo"] == id_no_to_update:
                
                print("\n- Teacher Found:\n")
                print(f"\tName: {teacher["Name"]}")
                print(f"\tSubject: {teacher['Subject']}")
                print(f"\tQualification: {teacher['Qualification']}")
                print(f"\tContact: {teacher['Contact']}")
                print(f"\tId No: {teacher['IdNo']}")
                print(f"\tEmail: {teacher['Email']}\n")
                
                print("\nEnter new data (Leave blank to keep current data):\n")
                
                Name = input("Enter Teacher Name: ")
                Subject = input("Enter Teacher Subject: ")
                Qualification = input("Enter Teacher Qualification: ")
                Contact = input("Enter Teacher's Contact Number: ")
                IdNo = input("Enter Teacher Id Number: ")
                Email = input("Enter Teacher Email: ")
                    
                teacher.update({
                    "Name": Name if Name else teacher["Name"],
                    "Subject": Subject if Subject else teacher["Subject"],
                    "Qualification": Qualification if Qualification else teacher["Qualification"],
                    "Contact": Contact if Contact else teacher["Contact"],
                    "IdNo": IdNo if IdNo else teacher["IdNo"],
                    "Email": Email if Email else teacher["Email"]
                    })
            
                print("\nTeacher data updated successfully!\n")
                
                print(f"\tName: {teacher["Name"]}")
                print(f"\tSubject: {teacher['Subject']}")
                print(f"\tQualification: {teacher['Qualification']}")
                print(f"\tContact: {teacher['Contact']}")
                print(f"\tId No: {teacher['IdNo']}")
                print(f"\tEmail: {teacher['Email']}\n")
            
                with open("Data/Teacher.json", "w") as file:
                    json.dump(teachers, file, indent=4)
                    
                found = True
                break
            
        if found:
            break
                
        else:
            print("\n** No teacher with such credentials found!\n")
            
            
            
            
            
def enter_teacher_portal():
    
    if not os.path.exists("Data/Teacher.json"):
        print("\n** No teacher data found. File does not exist.\n")
        return
    
    with open("Data/Teacher.json", "r") as file:
        teachers = json.load(file)
        
    
    if len(teachers) == 0:
        print("\n** No teachers found.\n")
        return
    
    
    
    while True:
    
        username = input("Enter Teacher Name: ")
        password = input("Enter Teacher Id Number: ")
        
        found = False
        
        for teacher in teachers:
            
            if teacher["Name"] == username and teacher["IdNo"] == password:
                print("\nLogin Successful!\n")
                
                print(f"\nWelcome to the Teacher Portal, {username}!\n")
                
                print(f"\tName: {teacher["Name"]}")
                print(f"\tSubject: {teacher['Subject']}")
                print(f"\tQualification: {teacher['Qualification']}")
                print(f"\tContact: {teacher['Contact']}")
                print(f"\tId No: {teacher['IdNo']}")
                print(f"\tEmail: {teacher['Email']}\n")
                
                found = True
                break
                
        if found:
            break
        
        else:
            print("\nInvalid credentials. Please try again.\n")
                
            
            