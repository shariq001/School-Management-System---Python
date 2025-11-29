import School
import Student
import Teacher
import Admin

print("\nHello and Welcome to Fusion Five Project!")

while True:
    
    print("What you want to access?")
    print("1. School Management")
    print("2. Student Portal")
    print("3. Teacher Portal")
    print("4. Admin Portal")
    print("5. Exit")
    
    print("\nOnly type operation number to proceed further (1 - 4).\n")
    
    choice = input()
    
    if choice == "1":
        School.main()
    elif choice == "2":
        Student.enter_student_portal()
    elif choice == "3":
        Teacher.enter_teacher_portal()
    elif choice == "4":
        Admin.enter_admin_portal()
    elif choice == "5":
        print("Exiting Project... Thank you!")
        break
    
    