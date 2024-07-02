"""
Teacher module for the Student Data Management System.
"""

import json
import re
from src.exceptions import NoMatchingNameError

def add_teacher():
    """
    Accept teacher information from the user and store it in a file.
    """
    name = input("Enter teacher's name: ")
    subject = input("Enter teacher's subject: ")
    id = input("Enter teacher's ID: ")
    address = input("Enter teacher's address: ")
    email = input("Enter teacher's email: ")
    phone_number = input("Enter teacher's phone number: ")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email address. Please try again.")
        return
    
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("Phone number must be 10 digits. Please try again.")
        return

    teacher = {
        "name": name,
        "subject": subject,
        "id": id,
        "address": address,
        "email": email,
        "phone_number": phone_number
    }

    with open('data_file/teachers.json', 'a') as f:
        json.dump(teacher, f)
        f.write('\n')
    print("Teacher added successfully.")

def display_all_teachers():
    """
    Display all teachers' general public information.
    """
    try:
        with open('data_file/teachers.json', 'r') as f:
            for line in f:
                teacher = json.loads(line)
                print(f"Name: {teacher['name']}, Subject: {teacher['subject']}, Email: {teacher['email']}, Phone: {teacher['phone_number']}")
    except FileNotFoundError:
        print("No teachers found.")

def search_teacher(name):
    """
    Search for a teacher by name and display full details.
    """
    found = False
    try:
        with open('data_file/teachers.json', 'r') as f:
            for line in f:
                teacher = json.loads(line)
                if teacher['name'] == name:
                    print(f"Name: {teacher['name']}, Subject: {teacher['subject']}, ID: {teacher['id']}, Address: {teacher['address']}, Email: {teacher['email']}, Phone: {teacher['phone_number']}")
                    found = True
                    break
        if not found:
            raise NoMatchingNameError(f"No teacher found with name: {name}")
    except FileNotFoundError:
        print("No teachers found.")

def delete_teacher(name):
    """
    Delete a teacher's record by name.
    """
    found = False
    teachers = []
    try:
        with open('data_file/teachers.json', 'r') as f:
            for line in f:
                teacher = json.loads(line)
                if teacher['name'] == name:
                    found = True
                else:
                    teachers.append(teacher)
        if not found:
            raise NoMatchingNameError(f"No teacher found with name: {name}")
        else:
            with open('data_file/teachers.json', 'w') as f:
                for teacher in teachers:
                    json.dump(teacher, f)
                    f.write('\n')
            print(f"Teacher {name} deleted successfully.")
    except FileNotFoundError:
        print("No teachers found.")
