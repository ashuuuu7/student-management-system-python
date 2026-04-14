class Student:

    def add_student(self):
        name = input("Enter the name of the new student you want to add")
        roll = int(input("Enter the roll number of the new student"))
        marks = int(input("Enter the new marks of the student"))
        with open("student.txt", "a") as f:
            f.write(f"\n{name}, {roll}, {marks}")

    def view_student(self):
        with open("student.txt") as f:
            students = f.read()
        print(students)

    def search_student(self):
        name = input("Enter the name of the student you want to get the details")
        roll = int(input("Enter the roll number of the same student"))

        found = False

        with open("student.txt") as f:
            lines = f.readlines()
            for line in lines:
                part = line.strip().split(", ")
                if part[0] == name and part[1] == str(roll):
                    print("Student data found")
                    print(line)
                    found = True
                    break
        if not found:
                print("No data found!")

    def upadte_marks(self):
        name = input("Enter the name of the student you want to upadate the marks")
        roll = int(input("Enter the roll number of the same student "))
        upadated_marks = int(input("Enter the new mark that you want to upadte in student details"))

        updated_data = []
        found = False

        with open("student.txt") as f :
            lines = f.readlines()
            for line in lines:
                part = line.strip().split(", ")
                if part[0] == name and part[1] == str(roll):
                    part[2] = str(upadated_marks)
                    new_line = ", ".join(part) + "\n"
                    updated_data.append(new_line)
                    found = True
                else:
                    updated_data.append(line)
            with open("student.txt" , "w") as f:
                f.writelines(updated_data)
            if found :
                print("Marks updated successfully")
            else:
                print("Data not found!")

    def delete_student(self):
        name = input("Enter the name of the student you want to delete the data")
        roll = int(input("Enter the roll number of the same student "))

        updated_data = []
        found = False

        with open("student.txt") as f:
            lines = f.readlines()
            for line in lines:
                part = line.strip().split(", ")
                if part[0] == name and part[1] == str(roll):
                    found = True
                    continue
                else:
                    updated_data.append(line)
            with open("student.txt" , "w") as f:
                f.writelines(updated_data)
            if found:
                print(f"{name}'s data has been deleted succesfully")
            else:
                print("Data not found!")

s = Student()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Student")   
    print("3. Search Student")    
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter you choice"))

    if choice == 1:
        s.add_student()
    elif choice == 2:
        s.view_student()
    elif choice == 3:
        s.search_student()
    elif choice == 4:
        s.upadte_marks()
    elif choice == 5:
        s.delete_student()
    elif choice == 6:
        print("Exicting Program")
        break
    else:
        print("Invalid Choice")