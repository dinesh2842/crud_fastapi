from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from pathlib import Path as SysPath
import json

app = FastAPI()

DB_FILE = SysPath('students.json')

# Load students from file if it exists
if DB_FILE.exists():
    with DB_FILE.open('r') as f:
        students = json.load(f)
else:
    students = {
        1: {"name": "john", "age": 25, "year": "10 D"}
    }


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


def save_students():
    """Helper function to save the students dict to file as JSON."""
    with DB_FILE.open('w') as f:
        json.dump(students, f, indent=2)


@app.get('/')
def index():
    return students


@app.get('/get-student/{student_id}')
def get_student(
    student_id: int = Path(..., description='The id of the student you want to view', gt=0)
):
    student = students.get(str(student_id))
    if not student:
        return {"error": "Student not found"}
    return student


@app.get('/get-by-name')
def get_by_name(name: Optional[str] = None):
    if name:
        for student_id, student in students.items():
            if student.get('name') == name:
                return student
        return {"error": "Student not found"}
    return list(students.values())


@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if str(student_id) in students:
        return {'error': 'Student exists'}
    students[str(student_id)] = student.dict()
    save_students()
    return students[str(student_id)]


@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if str(student_id) not in students:
        return {"error": "Student does not exist"}

    # update the fields
    if student.name is not None:
        students[str(student_id)]['name'] = student.name
    if student.age is not None:
        students[str(student_id)]['age'] = student.age
    if student.year is not None:
        students[str(student_id)]['year'] = student.year

    save_students()
    return students[str(student_id)]


@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if str(student_id) not in students:
        return {"error": "Student does not exist"}
    del students[str(student_id)]
    save_students()
    return {"message": "Student deleted successfully"}
