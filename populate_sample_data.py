#!/usr/bin/env python3
"""
Example script demonstrating how to use the School ERP System API.
This can serve as a template for building frontend applications.
"""

from app import create_app, db
from models import Student, Teacher, Course, Attendance, Grade
from datetime import datetime, date

def populate_sample_data():
    """Populate the database with sample data"""
    
    app = create_app('development')
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("Creating sample data...")
        
        # Create teachers
        teacher1 = Teacher(
            first_name="Sarah",
            last_name="Williams",
            email="sarah.williams@school.edu",
            phone="555-0001",
            subject_specialization="Mathematics",
            department="Mathematics"
        )
        
        teacher2 = Teacher(
            first_name="Michael",
            last_name="Davis",
            email="michael.davis@school.edu",
            phone="555-0002",
            subject_specialization="English",
            department="Languages"
        )
        
        db.session.add(teacher1)
        db.session.add(teacher2)
        db.session.commit()
        print(f"✓ Created {Teacher.query.count()} teachers")
        
        # Create courses
        course1 = Course(
            course_code="MATH201",
            course_name="Calculus I",
            description="Introduction to differential and integral calculus",
            credits=4,
            teacher_id=teacher1.id,
            semester="Fall 2024",
            schedule="MWF 09:00-10:00",
            room="Math Building 301"
        )
        
        course2 = Course(
            course_code="ENG101",
            course_name="English Literature",
            description="Survey of English literature from medieval to modern",
            credits=3,
            teacher_id=teacher2.id,
            semester="Fall 2024",
            schedule="TTh 11:00-12:30",
            room="Arts Building 105"
        )
        
        db.session.add(course1)
        db.session.add(course2)
        db.session.commit()
        print(f"✓ Created {Course.query.count()} courses")
        
        # Create students
        students_data = [
            {
                "first_name": "Emma",
                "last_name": "Thompson",
                "email": "emma.thompson@student.edu",
                "date_of_birth": date(2008, 4, 12),
                "grade_level": "11th Grade",
                "phone": "555-1001",
                "address": "123 Elm Street",
                "parent_name": "John Thompson",
                "parent_phone": "555-1002"
            },
            {
                "first_name": "Liam",
                "last_name": "Martinez",
                "email": "liam.martinez@student.edu",
                "date_of_birth": date(2008, 7, 23),
                "grade_level": "11th Grade",
                "phone": "555-1003",
                "address": "456 Oak Avenue",
                "parent_name": "Maria Martinez",
                "parent_phone": "555-1004"
            },
            {
                "first_name": "Olivia",
                "last_name": "Anderson",
                "email": "olivia.anderson@student.edu",
                "date_of_birth": date(2008, 1, 8),
                "grade_level": "11th Grade",
                "phone": "555-1005",
                "address": "789 Pine Road",
                "parent_name": "Robert Anderson",
                "parent_phone": "555-1006"
            }
        ]
        
        for student_data in students_data:
            student = Student(**student_data)
            db.session.add(student)
        
        db.session.commit()
        print(f"✓ Created {Student.query.count()} students")
        
        # Create attendance records
        students = Student.query.all()
        courses = Course.query.all()
        
        attendance_records = []
        for student in students:
            for course in courses:
                # Create attendance for past 5 days
                for days_ago in range(5):
                    attendance_date = date.today()
                    if days_ago > 0:
                        attendance_date = date(2024, 1, 15 + days_ago)
                    
                    status = "Present" if days_ago < 4 else "Late"
                    
                    attendance = Attendance(
                        student_id=student.id,
                        course_id=course.id,
                        date=attendance_date,
                        status=status,
                        notes=f"Regular class attendance" if status == "Present" else "Arrived 5 minutes late"
                    )
                    attendance_records.append(attendance)
        
        db.session.add_all(attendance_records)
        db.session.commit()
        print(f"✓ Created {Attendance.query.count()} attendance records")
        
        # Create grades
        grade_records = []
        assignments = [
            ("Quiz 1", 20, "First quiz on introductory material"),
            ("Homework 1", 15, "Weekly homework assignment"),
            ("Midterm Exam", 100, "Comprehensive midterm examination")
        ]
        
        for student in students:
            for course in courses:
                for assignment_name, max_grade, comments in assignments:
                    # Generate random-ish but realistic grades
                    base_grade = 75 + (hash(f"{student.id}{course.id}{assignment_name}") % 20)
                    grade_value = min(max_grade, base_grade * max_grade / 100)
                    
                    grade = Grade(
                        student_id=student.id,
                        course_id=course.id,
                        assignment_name=assignment_name,
                        grade_value=grade_value,
                        max_grade=max_grade,
                        comments=comments
                    )
                    grade_records.append(grade)
        
        db.session.add_all(grade_records)
        db.session.commit()
        print(f"✓ Created {Grade.query.count()} grade records")
        
        print("\n" + "="*60)
        print("Sample data created successfully!")
        print("="*60)
        print(f"\nDatabase Summary:")
        print(f"  - Students: {Student.query.count()}")
        print(f"  - Teachers: {Teacher.query.count()}")
        print(f"  - Courses: {Course.query.count()}")
        print(f"  - Attendance Records: {Attendance.query.count()}")
        print(f"  - Grade Records: {Grade.query.count()}")
        print("\nYou can now start the application with: python app.py")
        print("="*60 + "\n")

if __name__ == "__main__":
    populate_sample_data()
