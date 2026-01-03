# School ERP System

A comprehensive Enterprise Resource Planning (ERP) system for schools, built with Flask and SQLAlchemy. This system provides RESTful APIs for managing students, teachers, courses, attendance, and grades.

## Features

- **Student Management**: Create, read, update, and delete student records
- **Teacher Management**: Manage teacher information and assignments
- **Course Management**: Handle course creation, scheduling, and teacher assignments
- **Attendance Tracking**: Record and monitor student attendance
- **Grade Management**: Track student grades and assignments

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy with SQLite (easily configurable for PostgreSQL/MySQL)
- **API**: RESTful API with JSON responses
- **CORS**: Enabled for frontend integration

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Radhe70233984/School-ERP-System.git
cd School-ERP-System
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will start on `http://localhost:5000`

## API Documentation

### Base URL
```
http://localhost:5000
```

### Student Endpoints

#### Get All Students
```
GET /api/students
```

#### Get Single Student
```
GET /api/students/<student_id>
```

#### Create Student
```
POST /api/students
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "date_of_birth": "2010-05-15",
  "grade_level": "10th Grade",
  "phone": "123-456-7890",
  "address": "123 Main St",
  "parent_name": "Jane Doe",
  "parent_phone": "098-765-4321"
}
```

#### Update Student
```
PUT /api/students/<student_id>
Content-Type: application/json

{
  "grade_level": "11th Grade",
  "phone": "123-456-7890"
}
```

#### Delete Student
```
DELETE /api/students/<student_id>
```

### Teacher Endpoints

#### Get All Teachers
```
GET /api/teachers
```

#### Get Single Teacher
```
GET /api/teachers/<teacher_id>
```

#### Create Teacher
```
POST /api/teachers
Content-Type: application/json

{
  "first_name": "Jane",
  "last_name": "Smith",
  "email": "jane.smith@example.com",
  "phone": "555-123-4567",
  "subject_specialization": "Mathematics",
  "department": "Science"
}
```

#### Update Teacher
```
PUT /api/teachers/<teacher_id>
Content-Type: application/json

{
  "department": "Mathematics",
  "phone": "555-987-6543"
}
```

#### Delete Teacher
```
DELETE /api/teachers/<teacher_id>
```

### Course Endpoints

#### Get All Courses
```
GET /api/courses
```

#### Get Single Course
```
GET /api/courses/<course_id>
```

#### Create Course
```
POST /api/courses
Content-Type: application/json

{
  "course_code": "MATH101",
  "course_name": "Introduction to Algebra",
  "description": "Basic algebra concepts",
  "credits": 3,
  "teacher_id": 1,
  "semester": "Fall 2024",
  "schedule": "Mon/Wed 10:00-11:30",
  "room": "Room 101"
}
```

#### Update Course
```
PUT /api/courses/<course_id>
Content-Type: application/json

{
  "schedule": "Mon/Wed 14:00-15:30",
  "room": "Room 202"
}
```

#### Delete Course
```
DELETE /api/courses/<course_id>
```

### Attendance Endpoints

#### Get Attendance Records
```
GET /api/attendance
GET /api/attendance?student_id=1
GET /api/attendance?course_id=1
GET /api/attendance?date=2024-01-15
```

#### Get Single Attendance Record
```
GET /api/attendance/<attendance_id>
```

#### Create Attendance Record
```
POST /api/attendance
Content-Type: application/json

{
  "student_id": 1,
  "course_id": 1,
  "date": "2024-01-15",
  "status": "Present",
  "notes": "On time"
}
```

Status values: `Present`, `Absent`, `Late`, `Excused`

#### Update Attendance Record
```
PUT /api/attendance/<attendance_id>
Content-Type: application/json

{
  "status": "Late",
  "notes": "Arrived 10 minutes late"
}
```

#### Delete Attendance Record
```
DELETE /api/attendance/<attendance_id>
```

### Grade Endpoints

#### Get Grades
```
GET /api/grades
GET /api/grades?student_id=1
GET /api/grades?course_id=1
```

#### Get Single Grade
```
GET /api/grades/<grade_id>
```

#### Create Grade
```
POST /api/grades
Content-Type: application/json

{
  "student_id": 1,
  "course_id": 1,
  "assignment_name": "Midterm Exam",
  "grade_value": 85,
  "max_grade": 100,
  "comments": "Good work"
}
```

#### Update Grade
```
PUT /api/grades/<grade_id>
Content-Type: application/json

{
  "grade_value": 90,
  "comments": "Improved after review"
}
```

#### Delete Grade
```
DELETE /api/grades/<grade_id>
```

## Database Schema

### Students Table
- id (Primary Key)
- first_name
- last_name
- email (Unique)
- date_of_birth
- enrollment_date
- grade_level
- phone
- address
- parent_name
- parent_phone
- created_at
- updated_at

### Teachers Table
- id (Primary Key)
- first_name
- last_name
- email (Unique)
- phone
- subject_specialization
- hire_date
- department
- created_at
- updated_at

### Courses Table
- id (Primary Key)
- course_code (Unique)
- course_name
- description
- credits
- teacher_id (Foreign Key)
- semester
- schedule
- room
- created_at
- updated_at

### Attendance Table
- id (Primary Key)
- student_id (Foreign Key)
- course_id (Foreign Key)
- date
- status
- notes
- created_at

### Grades Table
- id (Primary Key)
- student_id (Foreign Key)
- course_id (Foreign Key)
- assignment_name
- grade_value
- max_grade
- grade_date
- comments
- created_at
- updated_at

## Configuration

The application can be configured through environment variables:

- `SECRET_KEY`: Secret key for Flask sessions (default: 'dev-secret-key-change-in-production')
- `DATABASE_URL`: Database connection URL (default: 'sqlite:///school_erp.db')
- `FLASK_ENV`: Environment mode - 'development' or 'production' (default: 'development')

## Development

### Running in Development Mode
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

### Running in Production Mode
```bash
export FLASK_ENV=production  # On Windows: set FLASK_ENV=production
python app.py
```

## Testing

You can test the API endpoints using tools like:
- cURL
- Postman
- HTTPie
- Or any HTTP client library

Example using cURL:
```bash
# Get all students
curl http://localhost:5000/api/students

# Create a new student
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "date_of_birth": "2010-05-15",
    "grade_level": "10th Grade"
  }'
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
