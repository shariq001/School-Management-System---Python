import json
import os

def add_admin():
    
    new_admin = {
        "Name" : input("Enter Admin Member Name: "),
        "Contact" : input("Enter Admin Member Contact Number: "),
        "Email" : input("Enter Admin Member Email: "),
        "Role" : input("Enter Admin Member Role: "),
        "Id": input("Enter Admin Member ID: ")
    }
    
    if os.path.exists("Data/Admin.json"):
        with open("Data/Admin.json", "r") as file:
            admins = json.load(file)
    else:
        admins = []


    admins.append(new_admin)
    
    with open("Data/Admin.json", "w") as file:
        json.dump(admins, file, indent=4)
        
    print("\n** Admin added successfully!\n")


def view_all_admins():
    
    if not os.path.exists("Data/Admin.json"):
        print("\n** No admin data found. File does not exist.\n")
        return
    
    
    with open("Data/Admin.json", "r") as file:
        admins = json.load(file)
        
    
    if len(admins) == 0:
        print("\n** No admins found.\n")
        return
    
    
    print("\n----> All Admins <----\n")
    
    for index, admin in enumerate(admins, start = 1):
        print(f"- Admin {index}: ")
        print(f"\tName: {admin["Name"]}")
        print(f"\tContact: {admin['Contact']}")
        print(f"\tEmail: {admin['Email']}")
        print(f"\tRole: {admin['Role']}")
        print(f"\tId: {admin['Id']}")
        print("----------------------------------")
        
        
        
def delete_an_admin():
    
    if not os.path.exists("Data/Admin.json"):
        print("\n** No admin data found. File does not exist.\n")
        return
    
    
    with open("Data/Admin.json", "r") as file:
        admins = json.load(file)
        
    
    if len(admins) == 0:
        print("\n** No admins found.\n")
        return
    
    condition1 = True
    
    while condition1:
    
        Id_to_delete = input("Enter the ID of admin to delete data: ")
        
        for admin in admins:
            
            if admin["Id"] == Id_to_delete:
                
                print("\n- Admin Found:\n")
                print(f"\tName: {admin["Name"]}")
                print(f"\tContact: {admin['Contact']}")
                print(f"\tEmail: {admin['Email']}")
                print(f"\tRole: {admin['Role']}")
                print(f"\tId: {admin['Id']}\n")
                
                choice3 = input("Do you want to delete data? (y/n): ").lower()
                
                if choice3 == "y":
                
                    admins.remove(admin)
                
                
                    with open("Data/Admin.json", "w") as file:
                        json.dump(admins, file, indent=4)
                    print("\nAdmin data deleted successfully!\n")
                    condition1 = False
                    return
                
                else:
                    print("\nDeletion Cancelled!\n")
                    condition1 = False
                    
            else:
                print("\n** No admin with such credentials found!\n")
        
        
        
def search_specific_admin():
    
    if not os.path.exists("Data/Admin.json"):
        print("\n** No admin data found. File does not exist.\n")
        return
    
    
    with open("Data/Admin.json", "r") as file:
        admins = json.load(file)
        
    
    if len(admins) == 0:
        print("\n** No admins found.\n")
        return
    
    condition2 = True
    
    while condition2:
    
        Id_to_search = input("Enter the ID of admin to search data: ")
        
        for admin in admins:
            
            if admin["Id"] == Id_to_search:
                print("\n- Admin Found:\n")
                print(f"\tName: {admin["Name"]}")
                print(f"\tContact: {admin['Contact']}")
                print(f"\tEmail: {admin['Email']}")
                print(f"\tRole: {admin['Role']}")
                print(f"\tId: {admin['Id']}\n")
                
                condition2 = False
                
            else:
                print("\n** No admin with such credentials found!\n")
            
            
            
def update_admin_data():
    
    if not os.path.exists("Data/Admin.json"):
        print("\n** No admin data found. File does not exist.\n")
        return
    
    
    with open("Data/Admin.json", "r") as file:
        admins = json.load(file)
        
    
    if len(admins) == 0:
        print("\n** No admins found.\n")
        return
    
    condition3 = True
    
    while condition3:
    
        Id_to_update = input("Enter the ID of admin to update data: ")
    
        for admin in admins: 
            
            if admin["Id"] == Id_to_update:
                
                print("\n- Admin Found:\n")
                print(f"\tName: {admin["Name"]}")
                print(f"\tContact: {admin['Contact']}")
                print(f"\tEmail: {admin['Email']}")
                print(f"\tRole: {admin['Role']}")
                print(f"\tId: {admin['Id']}")
                
                print("\nEnter new data (Leave blank to keep current data):\n")
                
                Name = input("Enter Admin Member Name: ")
                Contact = input("Enter Admin Member Contact Number: ")
                Email = input("Enter Admin Member Email: ")
                Role = input("Enter Admin Member Role: ")
                Id = input("Enter Admin Member ID: ")
                
                admin.update({
                    "Name": Name if Name else admin["Name"],
                    "Contact": Contact if Contact else admin["Contact"],
                    "Email": Email if Email else admin["Email"],
                    "Role": Role if Role else admin["Role"],
                    "Id": Id if Id else admin["Id"],
                })
            
                print("\nAdmin data updated successfully!\n")
                
                print(f"\tName: {admin["Name"]}")
                print(f"\tContact: {admin['Contact']}")
                print(f"\tEmail: {admin['Email']}")
                print(f"\tRole: {admin['Role']}")
                print(f"\tId: {admin['Id']}\n")
                
                with open("Data/Admin.json", "w") as file:
                    json.dump(admins, file, indent=4)
                    
                condition3 = False
                
            else:
                print("\n** No admin with such credentials found!\n")
            
            

def enter_admin_portal():
    
    
    
    if not os.path.exists("Data/Admin.json"):
        print("\n** No admin data found. File does not exist.\n")
        return
    
    
    with open("Data/Admin.json", "r") as file:
        admins = json.load(file)
        
    
    if len(admins) == 0:
        print("\n** No admins found.\n")
        return
    
    condition4 = True
    
    while condition4:
    
        username = input("Enter Admin Name: ")
        password = input("Enter Id Number: ")
        
        for admin in admins:
            
            if admin["Name"] == username and admin["Id"] == password:
                print("\nLogin successful!\n")
                print(f"\nWelcome to the Admin Portal, {username}!\n")
                
                print(f"\tName: {admin["Name"]}")
                print(f"\tContact: {admin['Contact']}")
                print(f"\tEmail: {admin['Email']}")
                print(f"\tRole: {admin['Role']}")
                print(f"\tId: {admin['Id']}\n")
                
                condition4 = False
                
            else:
                print("\nInvalid credentials. Please try again.")     