from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, date
from config import config
from models import db, Student, Teacher, Course, Attendance, Grade
import os

def create_app(config_name='default'):
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    # Home route
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to School ERP System API',
            'version': '1.0',
            'endpoints': {
                'students': '/api/students',
                'teachers': '/api/teachers',
                'courses': '/api/courses',
                'attendance': '/api/attendance',
                'grades': '/api/grades'
            }
        })
    
    # Student routes
    @app.route('/api/students', methods=['GET'])
    def get_students():
        students = Student.query.all()
        return jsonify([student.to_dict() for student in students])
    
    @app.route('/api/students/<int:student_id>', methods=['GET'])
    def get_student(student_id):
        student = Student.query.get_or_404(student_id)
        return jsonify(student.to_dict())
    
    @app.route('/api/students', methods=['POST'])
    def create_student():
        data = request.get_json()
        
        try:
            student = Student(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date(),
                grade_level=data['grade_level'],
                phone=data.get('phone'),
                address=data.get('address'),
                parent_name=data.get('parent_name'),
                parent_phone=data.get('parent_phone')
            )
            
            db.session.add(student)
            db.session.commit()
            
            return jsonify(student.to_dict()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/students/<int:student_id>', methods=['PUT'])
    def update_student(student_id):
        student = Student.query.get_or_404(student_id)
        data = request.get_json()
        
        try:
            if 'first_name' in data:
                student.first_name = data['first_name']
            if 'last_name' in data:
                student.last_name = data['last_name']
            if 'email' in data:
                student.email = data['email']
            if 'date_of_birth' in data:
                student.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
            if 'grade_level' in data:
                student.grade_level = data['grade_level']
            if 'phone' in data:
                student.phone = data['phone']
            if 'address' in data:
                student.address = data['address']
            if 'parent_name' in data:
                student.parent_name = data['parent_name']
            if 'parent_phone' in data:
                student.parent_phone = data['parent_phone']
            
            db.session.commit()
            return jsonify(student.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/students/<int:student_id>', methods=['DELETE'])
    def delete_student(student_id):
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200
    
    # Teacher routes
    @app.route('/api/teachers', methods=['GET'])
    def get_teachers():
        teachers = Teacher.query.all()
        return jsonify([teacher.to_dict() for teacher in teachers])
    
    @app.route('/api/teachers/<int:teacher_id>', methods=['GET'])
    def get_teacher(teacher_id):
        teacher = Teacher.query.get_or_404(teacher_id)
        return jsonify(teacher.to_dict())
    
    @app.route('/api/teachers', methods=['POST'])
    def create_teacher():
        data = request.get_json()
        
        try:
            teacher = Teacher(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                phone=data.get('phone'),
                subject_specialization=data.get('subject_specialization'),
                department=data.get('department')
            )
            
            db.session.add(teacher)
            db.session.commit()
            
            return jsonify(teacher.to_dict()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/teachers/<int:teacher_id>', methods=['PUT'])
    def update_teacher(teacher_id):
        teacher = Teacher.query.get_or_404(teacher_id)
        data = request.get_json()
        
        try:
            if 'first_name' in data:
                teacher.first_name = data['first_name']
            if 'last_name' in data:
                teacher.last_name = data['last_name']
            if 'email' in data:
                teacher.email = data['email']
            if 'phone' in data:
                teacher.phone = data['phone']
            if 'subject_specialization' in data:
                teacher.subject_specialization = data['subject_specialization']
            if 'department' in data:
                teacher.department = data['department']
            
            db.session.commit()
            return jsonify(teacher.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/teachers/<int:teacher_id>', methods=['DELETE'])
    def delete_teacher(teacher_id):
        teacher = Teacher.query.get_or_404(teacher_id)
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({'message': 'Teacher deleted successfully'}), 200
    
    # Course routes
    @app.route('/api/courses', methods=['GET'])
    def get_courses():
        courses = Course.query.all()
        return jsonify([course.to_dict() for course in courses])
    
    @app.route('/api/courses/<int:course_id>', methods=['GET'])
    def get_course(course_id):
        course = Course.query.get_or_404(course_id)
        return jsonify(course.to_dict())
    
    @app.route('/api/courses', methods=['POST'])
    def create_course():
        data = request.get_json()
        
        try:
            course = Course(
                course_code=data['course_code'],
                course_name=data['course_name'],
                description=data.get('description'),
                credits=data.get('credits', 3),
                teacher_id=data.get('teacher_id'),
                semester=data.get('semester'),
                schedule=data.get('schedule'),
                room=data.get('room')
            )
            
            db.session.add(course)
            db.session.commit()
            
            return jsonify(course.to_dict()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/courses/<int:course_id>', methods=['PUT'])
    def update_course(course_id):
        course = Course.query.get_or_404(course_id)
        data = request.get_json()
        
        try:
            if 'course_code' in data:
                course.course_code = data['course_code']
            if 'course_name' in data:
                course.course_name = data['course_name']
            if 'description' in data:
                course.description = data['description']
            if 'credits' in data:
                course.credits = data['credits']
            if 'teacher_id' in data:
                course.teacher_id = data['teacher_id']
            if 'semester' in data:
                course.semester = data['semester']
            if 'schedule' in data:
                course.schedule = data['schedule']
            if 'room' in data:
                course.room = data['room']
            
            db.session.commit()
            return jsonify(course.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/courses/<int:course_id>', methods=['DELETE'])
    def delete_course(course_id):
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 200
    
    # Attendance routes
    @app.route('/api/attendance', methods=['GET'])
    def get_attendance():
        student_id = request.args.get('student_id', type=int)
        course_id = request.args.get('course_id', type=int)
        date_str = request.args.get('date')
        
        query = Attendance.query
        
        if student_id:
            query = query.filter_by(student_id=student_id)
        if course_id:
            query = query.filter_by(course_id=course_id)
        if date_str:
            query = query.filter_by(date=datetime.strptime(date_str, '%Y-%m-%d').date())
        
        attendance_records = query.all()
        return jsonify([record.to_dict() for record in attendance_records])
    
    @app.route('/api/attendance/<int:attendance_id>', methods=['GET'])
    def get_attendance_record(attendance_id):
        record = Attendance.query.get_or_404(attendance_id)
        return jsonify(record.to_dict())
    
    @app.route('/api/attendance', methods=['POST'])
    def create_attendance():
        data = request.get_json()
        
        try:
            attendance = Attendance(
                student_id=data['student_id'],
                course_id=data['course_id'],
                date=datetime.strptime(data.get('date', datetime.utcnow().strftime('%Y-%m-%d')), '%Y-%m-%d').date(),
                status=data['status'],
                notes=data.get('notes')
            )
            
            db.session.add(attendance)
            db.session.commit()
            
            return jsonify(attendance.to_dict()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/attendance/<int:attendance_id>', methods=['PUT'])
    def update_attendance(attendance_id):
        record = Attendance.query.get_or_404(attendance_id)
        data = request.get_json()
        
        try:
            if 'status' in data:
                record.status = data['status']
            if 'notes' in data:
                record.notes = data['notes']
            if 'date' in data:
                record.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
            
            db.session.commit()
            return jsonify(record.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/attendance/<int:attendance_id>', methods=['DELETE'])
    def delete_attendance(attendance_id):
        record = Attendance.query.get_or_404(attendance_id)
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Attendance record deleted successfully'}), 200
    
    # Grade routes
    @app.route('/api/grades', methods=['GET'])
    def get_grades():
        student_id = request.args.get('student_id', type=int)
        course_id = request.args.get('course_id', type=int)
        
        query = Grade.query
        
        if student_id:
            query = query.filter_by(student_id=student_id)
        if course_id:
            query = query.filter_by(course_id=course_id)
        
        grades = query.all()
        return jsonify([grade.to_dict() for grade in grades])
    
    @app.route('/api/grades/<int:grade_id>', methods=['GET'])
    def get_grade(grade_id):
        grade = Grade.query.get_or_404(grade_id)
        return jsonify(grade.to_dict())
    
    @app.route('/api/grades', methods=['POST'])
    def create_grade():
        data = request.get_json()
        
        try:
            grade = Grade(
                student_id=data['student_id'],
                course_id=data['course_id'],
                assignment_name=data['assignment_name'],
                grade_value=data['grade_value'],
                max_grade=data.get('max_grade', 100.0),
                comments=data.get('comments')
            )
            
            db.session.add(grade)
            db.session.commit()
            
            return jsonify(grade.to_dict()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/grades/<int:grade_id>', methods=['PUT'])
    def update_grade(grade_id):
        grade = Grade.query.get_or_404(grade_id)
        data = request.get_json()
        
        try:
            if 'assignment_name' in data:
                grade.assignment_name = data['assignment_name']
            if 'grade_value' in data:
                grade.grade_value = data['grade_value']
            if 'max_grade' in data:
                grade.max_grade = data['max_grade']
            if 'comments' in data:
                grade.comments = data['comments']
            
            db.session.commit()
            return jsonify(grade.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/grades/<int:grade_id>', methods=['DELETE'])
    def delete_grade(grade_id):
        grade = Grade.query.get_or_404(grade_id)
        db.session.delete(grade)
        db.session.commit()
        return jsonify({'message': 'Grade deleted successfully'}), 200
    
    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    app.run(host='0.0.0.0', port=5000)
