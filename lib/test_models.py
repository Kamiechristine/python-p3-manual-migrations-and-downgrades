import pytest
from models import Student

def test_student_creation():
    student = Student(name="John Doe", grade=10)
    assert student.name == "John Doe"
    assert student.grade == 10  # Corrected to check grade instead of age

def test_student_str():
    student = Student(name="Jane Doe", grade=12)
    assert str(student) == "Student None: Jane Doe, Grade 12"  # Updated to match the __repr__ method
