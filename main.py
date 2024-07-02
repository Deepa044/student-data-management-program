"""
Main program for the Student Data Management System.
"""

import json
from src.teacher import add_teacher, display_all_teachers, search_teacher, delete_teacher
from src.student import add_student, display_all_students, search_student, calculate_ranks,delete_student
from src.exceptions import AuthenticationError, NoMatchingNameError

def initialize_first_teacher():
    """
    Initialize the first teacher if the teachers.json file is empty or does not exist.
    """
    try:
        with open('data_file/teachers.json', 'r') as f:
            if f.read().strip():
                return
    except FileNotFoundError:
        pass

    print("No teachers found. Please add the first teacher.")
    add_teacher()

def main():
    """
    Main function to run the Student Data Management System.
    """
    print("Welcome to the Student Data Management System")

    initialize_first_teacher()

    while True:
        print("\n1. Authenticate as Teacher")
        print("2. View Public Information (Students)")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            id = input("Enter your ID: ")
            authenticated = False
            try:
                with open('data_file/teachers.json', 'r') as f:
                    for line in f:
                        teacher = json.loads(line)
                        if teacher['name'] == name and teacher['id'] == id:
                            authenticated = True
                            break
                if not authenticated:
                    raise AuthenticationError()
            except FileNotFoundError:
                print("Teachers file not found")
            except AuthenticationError:
                print("Authentication failed. Invalid name or ID.")
            else:
                print(f"Welcome {name}!")
                while authenticated:
                    print("\n1. Add Teacher")
                    print("2. Add Student")
                    print("3. Display All Teachers")
                    print("4. Display All Students")
                    print("5. Search Teacher by Name")
                    print("6. Search Student by Name")
                    print("7. Delete Teacher by Name")
                    print("8. Delete Student by Name")
                    print("9. Calculate and Display Student Ranks")
                    print("10. Log Out")
                    teacher_choice = input("Enter your choice: ")

                    if teacher_choice == '1':
                        add_teacher()
                    elif teacher_choice == '2':
                        add_student()
                    elif teacher_choice == '3':
                        display_all_teachers()
                    elif teacher_choice == '4':
                        display_all_students()
                    elif teacher_choice == '5':
                        name = input("Enter teacher's name to search: ")
                        try:
                            search_teacher(name)
                        except NoMatchingNameError as e:
                            print(e)
                    elif teacher_choice == '6':
                        name = input("Enter student's name to search: ")
                        try:
                            search_student(name)
                        except NoMatchingNameError as e:
                            print(e)
                    elif teacher_choice == '7':
                        name = input("Enter teacher's name to delete: ")
                        try:
                            delete_teacher(name)
                        except NoMatchingNameError as e:
                            print(e)
                    elif teacher_choice == '8':
                        name = input("Enter student's name to delete: ")
                        try:
                            delete_student(name)
                        except NoMatchingNameError as e:
                            print(e)
                    elif teacher_choice == '9':
                        calculate_ranks()
                    elif teacher_choice == '10':
                        authenticated = False
                        print("Logged out successfully.")
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '2':
            print("\nPublic Information (Students):")
            display_all_students()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

