from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from database import db


def serialize_course(course):
    course["_id"] = str(course["_id"])
    return course


# CREATE
@api_view(["POST"])
def create_course(request):

    course = request.data

    result = db.course.insert_one(course)

    return Response(
        {
            "message": "Course created successfully",
            "id": str(result.inserted_id)
        },
        status=status.HTTP_201_CREATED
    )


# READ ALL
@api_view(["GET"])
def get_courses(request):

    courses = list(db.course.find())

    for course in courses:
        serialize_course(course)

    return Response(courses)


# READ ONE
@api_view(["GET"])
def get_course(request, course_id):

    course = db.course.find_one({
        "course_id": course_id
    })

    if not course:
        return Response(
            {"message": "Course not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serialize_course(course)

    return Response(course)


# UPDATE
@api_view(["PUT"])
def update_course(request, course_id):

    result = db.course.update_one(
        {"course_id": course_id},
        {"$set": request.data}
    )

    if result.matched_count == 0:
        return Response(
            {"message": "Course not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "message": "Course updated successfully"
    })


# DELETE
@api_view(["DELETE"])
def delete_course(request, course_id):

    result = db.course.delete_one({
        "course_id": course_id
    })

    if result.deleted_count == 0:
        return Response(
            {"message": "Course not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "message": "Course deleted successfully"
    })
