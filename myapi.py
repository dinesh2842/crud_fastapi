from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students={
    1:{
        'name':'john',
        'age':25,
        'year':'10 D'
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year:Optional[str] = None

@app.get('/')
def index():
    return {"name":'dinesh','age':23}

@app.get('/get-student/{student_id}')
def get_student(student_id:int = Path(...,description = 'The id of the student you want to view',gt=0,lt=3)):
    return students[student_id]


@app.get('/get-by-name{student_id}')
def get_student(*, student_id:int, name: Optional[str]=None,test:int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data":"Not found"}

#this one is create a new object in the database
@app.post('/create-student/{student_id}')
def create_student(student_id:int , student : Student):
    if student_id in students: #this wont allow you to create the object with existind id 
        return {'error':'students exist'}
    
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int,student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Students does not exists"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id:int):
    if student_id not in students:
        return {"error":"Student does not exist"}
    del students[student_id]
    return {"message":"student deleted successfully"}
    







