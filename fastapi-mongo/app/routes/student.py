from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.controllers.student import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from app.schemas.student import (
    StudentSchema,
    UpdateStudentModel,
)
from app.models.student import (
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    from fastapi.encoders import jsonable_encoder
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


@router.get("/", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students retrieved successfully.")
    return ResponseModel(students, "Empty list returned")


@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id: str):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student data retrieved successfully.")
    return ErrorResponseModel("An error occurred.", 404, "Student does not exist.")


@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = jsonable_encoder(req)
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(updated_student, "Student updated successfully.")
    return ErrorResponseModel("An error occurred.", 404, "Student does not exist.")


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(deleted_student, "Student deleted successfully.")
    return ErrorResponseModel("An error occurred.", 404, "Student does not exist.")
