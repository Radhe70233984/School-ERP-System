#!/usr/bin/env python3
"""
Simple test script to demonstrate School ERP System functionality.
This script tests all the main API endpoints.
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"

def print_response(response, operation):
    """Print formatted response"""
    print(f"\n{'='*60}")
    print(f"Operation: {operation}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2))
    print(f"{'='*60}")

def test_school_erp_system():
    """Test all main endpoints"""
    
    print("\n" + "="*60)
    print("TESTING SCHOOL ERP SYSTEM")
    print("="*60)
    
    # Test home endpoint
    response = requests.get(f"{BASE_URL}/")
    print_response(response, "GET / - Home")
    
    # Create a student
    student_data = {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@example.com",
        "date_of_birth": "2011-03-20",
        "grade_level": "9th Grade",
        "phone": "111-222-3333",
        "address": "456 Oak Ave",
        "parent_name": "Bob Johnson",
        "parent_phone": "111-222-4444"
    }
    response = requests.post(f"{BASE_URL}/api/students", json=student_data)
    print_response(response, "POST /api/students - Create Student")
    student_id = response.json()['id']
    
    # Get all students
    response = requests.get(f"{BASE_URL}/api/students")
    print_response(response, "GET /api/students - Get All Students")
    
    # Create a teacher
    teacher_data = {
        "first_name": "Robert",
        "last_name": "Brown",
        "email": "robert.brown@example.com",
        "phone": "555-987-6543",
        "subject_specialization": "Physics",
        "department": "Science"
    }
    response = requests.post(f"{BASE_URL}/api/teachers", json=teacher_data)
    print_response(response, "POST /api/teachers - Create Teacher")
    teacher_id = response.json()['id']
    
    # Get all teachers
    response = requests.get(f"{BASE_URL}/api/teachers")
    print_response(response, "GET /api/teachers - Get All Teachers")
    
    # Create a course
    course_data = {
        "course_code": "PHYS101",
        "course_name": "Introduction to Physics",
        "description": "Basic physics concepts and principles",
        "credits": 4,
        "teacher_id": teacher_id,
        "semester": "Spring 2024",
        "schedule": "Tue/Thu 14:00-15:30",
        "room": "Lab 201"
    }
    response = requests.post(f"{BASE_URL}/api/courses", json=course_data)
    print_response(response, "POST /api/courses - Create Course")
    course_id = response.json()['id']
    
    # Get all courses
    response = requests.get(f"{BASE_URL}/api/courses")
    print_response(response, "GET /api/courses - Get All Courses")
    
    # Create attendance record
    attendance_data = {
        "student_id": student_id,
        "course_id": course_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "status": "Present",
        "notes": "Active participation"
    }
    response = requests.post(f"{BASE_URL}/api/attendance", json=attendance_data)
    print_response(response, "POST /api/attendance - Create Attendance")
    
    # Get attendance for student
    response = requests.get(f"{BASE_URL}/api/attendance?student_id={student_id}")
    print_response(response, f"GET /api/attendance?student_id={student_id} - Get Student Attendance")
    
    # Create grade record
    grade_data = {
        "student_id": student_id,
        "course_id": course_id,
        "assignment_name": "Quiz 1",
        "grade_value": 92,
        "max_grade": 100,
        "comments": "Excellent understanding of concepts"
    }
    response = requests.post(f"{BASE_URL}/api/grades", json=grade_data)
    print_response(response, "POST /api/grades - Create Grade")
    
    # Get grades for student
    response = requests.get(f"{BASE_URL}/api/grades?student_id={student_id}")
    print_response(response, f"GET /api/grades?student_id={student_id} - Get Student Grades")
    
    # Update student
    update_data = {"grade_level": "10th Grade"}
    response = requests.put(f"{BASE_URL}/api/students/{student_id}", json=update_data)
    print_response(response, f"PUT /api/students/{student_id} - Update Student")
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        test_school_erp_system()
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server.")
        print("Please make sure the Flask application is running on http://localhost:5000")
        print("Run: python app.py")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
