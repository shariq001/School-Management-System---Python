import Student
import Teacher
import Library
import Admin

def main():
    username = "admin"
    password = "admin123"

    user_input1 = input("Enter Username (# admin): ")
    user_input2 = input("Enter Password (# admin123): ")

    if user_input1 == username and user_input2 == password:
        
        print("\n----> Welcome to School Management System by Fusion Five! <----\n")    
        
        while True: 

            print("What would you like to do?")
            print("1. Students Management")
            print("2. Teachers Management")
            print("3. Library Management")
            print("4. Administration Management")
            print("5. Exit")
            print("\nOnly type operation number to proceed further.\n")

            choice1 = input("Enter your choice: ")
            
            if choice1 == "1":
                
                print("\n----> Welcome to Students Management System! <----\n")
                
                while True:
            
                    print("  Select an operation to perform:")
                    print("  1. Add a Student")
                    print("  2. View All Students")
                    print("  3. Delete a Student")
                    print("  4. Search Specific Student Data")
                    print("  5. Update Student Data")
                    print("  6. Exit")
                    print("\n  Online type operation number to proceed further (1 - 6).\n")
                    
                    choice2 = input("  Enter your choice: ")
                    
                    if choice2 == "1":
                        Student.add_student()
                    elif choice2 == "2":
                        Student.view_all_students()
                    elif choice2 == "3":
                        Student.delete_a_student()
                    elif choice2 == "4":
                        Student.search_specific_student()
                    elif choice2 == "5":
                        Student.update_student_data()
                    elif choice2 == "6":
                        print("\n** Exiting Students Management System.... Goodbye!\n")
                        break
                    
                    
            elif choice1 == "2":
                
                print("\n----> Welcome to Teacher Management System! <----\n")
                
                while True:
            
                    print("  Select an operation to perform:")
                    print("  1. Add a Teacher")
                    print("  2. View All Teachers")
                    print("  3. Delete a Teacher")
                    print("  4. Search Specific Teacher Data")
                    print("  5. Update Teacher Data")
                    print("  6. Exit")
                    print("\n  Online type operation number to proceed further (1 - 6).\n")
                    
                    choice2 = input("  Enter your choice: ")
                    
                    if choice2 == "1":
                        Teacher.add_teacher()
                    elif choice2 == "2":
                        Teacher.view_all_teachers()
                    elif choice2 == "3":
                        Teacher.delete_a_teacher()
                    elif choice2 == "4":
                        Teacher.search_specific_teacher()
                    elif choice2 == "5":
                        Teacher.update_teacher_data()
                    elif choice2 == "6":
                        print("\n** Exiting Teachers Management System.... Goodbye!\n")
                        break


            elif choice1 == "3":
                
                print("\n----> Welcome to Library Management System! <----\n")
                
                while True:
            
                    print("  Select an operation to perform:")
                    print("  1. Add a Book")
                    print("  2. View All Books")
                    print("  3. Delete a Book")
                    print("  4. Search Specific Book")
                    print("  5. Update Book Data")
                    print("  6. Exit")
                    print("\n  Online type operation number to proceed further (1 - 6).\n")
                    
                    choice2 = input("  Enter your choice: ")
                    
                    if choice2 == "1":
                        Library.add_book()
                    elif choice2 == "2":
                        Library.view_all_books()
                    elif choice2 == "3":
                        Library.delete_a_book()
                    elif choice2 == "4":
                        Library.search_specific_book()
                    elif choice2 == "5":
                        Library.update_book_data()
                    elif choice2 == "6":
                        print("\n** Exiting Library Management System.... Goodbye!\n")
                        break
                    
            
            elif choice1 == "4":
                
                print("\n----> Welcome to Admin Management System! <----\n")
                
                while True:
            
                    print("  Select an operation to perform:")
                    print("  1. Add an Admin")
                    print("  2. View All Admins")
                    print("  3. Delete a Admin")
                    print("  4. Search Specific Admin Data")
                    print("  5. Update Admin Data")
                    print("  6. Exit")
                    print("\n  Online type operation number to proceed further (1 - 6).\n")
                    
                    choice2 = input("  Enter your choice: ")
                    
                    if choice2 == "1":
                        Admin.add_admin()
                    elif choice2 == "2":
                        Admin.view_all_admins()
                    elif choice2 == "3":
                        Admin.delete_an_admin()
                    elif choice2 == "4":
                        Admin.search_specific_admin()
                    elif choice2 == "5":
                        Admin.update_admin_data()
                    elif choice2 == "6":
                        print("\n** Exiting Admins Management System.... Goodbye!\n")
                        break


            elif choice1 == "5":
                print("\n** Exiting Student Management System.... Thank you!\n")
                break

    else:
        print("\nInvalid credentials. Access denied.\n")
    