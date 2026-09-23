from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from database import db


def serialize_student(student):
    student["_id"] = str(student["_id"])
    return student


@api_view(["POST"])
def create_student(request):
    student = request.data

    result = db.students.insert_one(student)

    return Response(
        {
            "message": "Student created successfully",
            "id": str(result.inserted_id)
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def get_students(request):
    students = list(db.students.find())

    for student in students:
        serialize_student(student)

    return Response(students)


@api_view(["GET"])
def get_student(request, student_id):
    student = db.students.find_one({
        "student_id": student_id
    })

    if not student:
        return Response(
            {"message": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serialize_student(student)

    return Response(student)


@api_view(["PUT"])
def update_student(request, student_id):
    result = db.students.update_one(
        {"student_id": student_id},
        {"$set": request.data}
    )

    if result.matched_count == 0:
        return Response(
            {"message": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "message": "Student updated successfully"
    })


@api_view(["DELETE"])
def delete_student(request, student_id):
    result = db.students.delete_one({
        "student_id": student_id
    })

    if result.deleted_count == 0:
        return Response(
            {"message": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "message": "Student deleted successfully"
    })