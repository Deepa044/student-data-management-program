"""
Student module for the Student Data Management System.
"""

import json
import re
from src.exceptions import NoMatchingNameError

def add_student():
    """
    Accept student information from the user and store it in a file.
    """
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    email = input("Enter student's email: ")
    phone_number = input("Enter student's phone number: ")
    marks = input("Enter student's percentage : ")
    address = input("Enter student's address: ")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email address. Please try again.")
        return
    
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("Phone number must be 10 digits. Please try again.")
        return

    student = {
        "name": name,
        "roll_number": roll_number,
        "email": email,
        "phone_number": phone_number,
        "percentage": marks,
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
                    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Email: {student['email']}, Phone: {student['phone_number']}, Percentage: {student['marks']}, Address: {student['address']}")
                    found = True
                    break
        if not found:
            raise NoMatchingNameError(f"No student found with name: {name}")
    except FileNotFoundError:
        print("No students found.")

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


def calculate_ranks():
    """
    Calculate and display ranks based on students' marks.
    """
    try:
        with open('data_file/students.json', 'r') as f:
            students = [json.loads(line) for line in f]
        if not students:
            print("No students found.")
            return
        students.sort(key=lambda s: int(s['marks']), reverse=True)
        print("Rankings based on marks:")
        for rank, student in enumerate(students, start=1):
            print(f"Rank {rank}: {student['name']} - Percentage: {student['marks']}")
    except FileNotFoundError:
        print("No students found.")

