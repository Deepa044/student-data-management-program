"""
Student module for the Student Data Management System.
"""

import json
import re
from src.exceptions import NoMatchingNameError, NoMatchingIdError, AuthenticationError

def add_student():
    """
    Accept student information from the user and store it in a file.
    """
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    email = input("Enter student's email: ")
    phone_number = input("Enter student's phone number: ")
    mathematics_marks = input("Enter student's Mathematics marks: ")
    chemistry_marks = input("Enter student's Chemistry marks: ")
    physics_marks = input("Enter student's Physics marks: ")
    address = input("Enter student's address: ")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email address. Please try again.")
        return
    
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("Phone number must be 10 digits. Please try again.")
        return

    try:
        mathematics_marks = float(mathematics_marks)
        chemistry_marks = float(chemistry_marks)
        physics_marks = float(physics_marks)
    except ValueError:
        print("Marks must be numbers. Please try again.")
        return

    total_marks = mathematics_marks + chemistry_marks + physics_marks
    percentage = total_marks / 3  # Assuming each subject is out of 100

    student = {
        "name": name,
        "roll_number": roll_number,
        "email": email,
        "phone_number": phone_number,
        "mathematics_marks": mathematics_marks,
        "chemistry_marks": chemistry_marks,
        "physics_marks": physics_marks,
        "percentage": percentage,
        "address": address
    }

    with open('data_file/students.json', 'a') as f:
        json.dump(student, f)
        f.write('\n')
    print("Student added successfully.")

def display_all_students():
    """
    Display all students' general public information.
    """
    try:
        with open('data_file/students.json', 'r') as f:
            for line in f:
                student = json.loads(line)
                print(f"Name: {student['name']}, Email: {student['email']}, Phone: {student['phone_number']}")
    except FileNotFoundError:
        print("No students found.")

def search_student(name):
    """
    Search for a student by name and display full details.
    """
    found = False
    try:
        with open('data_file/students.json', 'r') as f:
            for line in f:
                student = json.loads(line)
                if student['name'] == name:
                    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Email: {student['email']}, Phone: {student['phone_number']}, Mathematics Marks: {student['mathematics_marks']}, Chemistry Marks: {student['chemistry_marks']}, Physics Marks: {student['physics_marks']}, Percentage: {student['percentage']:.2f}%, Address: {student['address']}")
                    found = True
                    break
        if not found:
            raise NoMatchingNameError(f"No student found with name: {name}")
    except FileNotFoundError:
        print("No students found.")
    except NoMatchingNameError as e:
        print(e)

def calculate_ranks():
    """
    Calculate and display ranks based on students' percentages.
    """
    try:
        with open('data_file/students.json', 'r') as f:
            students = [json.loads(line) for line in f]
        
        if not students:
            print("No students found.")
            return

        # Ensure all students have the 'percentage' key and its value is valid
        valid_students = []
        for student in students:
            if 'percentage' in student and isinstance(student['percentage'], (int, float)):
                valid_students.append(student)
            else:
                print(f"Incomplete or invalid data for student: {student}")

        if not valid_students:
            print("No valid student data to calculate ranks.")
            return

        # Sort students by percentage
        valid_students.sort(key=lambda s: float(s['percentage']), reverse=True)

        print("Rankings based on percentage:")
        for rank, student in enumerate(valid_students, start=1):
            print(f"Rank {rank}: {student['name']} - Percentage: {student['percentage']:.2f}%")
    
    except FileNotFoundError:
        print("No students found.")
    except json.JSONDecodeError:
        print("Error reading students data.")

def display_subject_teachers():
    """
    Display students and their subject teachers.
    """
    try:
        with open('data_file/students.json', 'r') as sf, open('data/teachers.json', 'r') as tf:
            students = [json.loads(line) for line in sf]
            teachers = [json.loads(line) for line in tf]
        if not students or not teachers:
            print("No students or teachers found.")
            return
        for student in students:
            print(f"Student: {student['name']}")
            print("Subject Teachers:")
            for teacher in teachers:
                print(f"Subject: {teacher['subject']}, Teacher: {teacher['name']}")
    except FileNotFoundError:
        print("No students or teachers found.")
    except json.JSONDecodeError:
        print("Error reading students or teachers data.")


def delete_student(name):
    """
    Delete a students's record by name.
    """
    found = False
    students = []
    try:
        with open('data_file/students.json', 'r') as f:
            for line in f:
                student = json.loads(line)
                if  student['name'] == name:
                    found = True
                else:
                    students.append(student)
        if not found:
            raise NoMatchingNameError(f"No  student found with name: {name}")
        else:
            with open('data_file/students.json', 'w') as f:
                for student in students:
                    json.dump(student, f)
                    f.write('\n')
            print(f"Student {name} deleted successfully.")
    except FileNotFoundError:
        print("No  students found.")


