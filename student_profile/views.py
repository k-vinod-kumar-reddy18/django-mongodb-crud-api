from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from database import db


def serialize_profile(profile):
    profile["_id"] = str(profile["_id"])
    return profile


# CREATE
@api_view(["POST"])
def create_profile(request):

    profile = request.data

    result = db.student_profile.insert_one(profile)

    return Response(
        {
            "message": "Student profile created successfully",
            "id": str(result.inserted_id)
        },
        status=status.HTTP_201_CREATED
    )


# READ ALL
@api_view(["GET"])
def get_profiles(request):

    profiles = list(db.student_profile.find())

    for profile in profiles:
        serialize_profile(profile)

    return Response(profiles)


# READ ONE
@api_view(["GET"])
def get_profile(request, student_id):

    profile = db.student_profile.find_one({
        "student_id": student_id
    })

    if not profile:
        return Response(
            {"message": "Student profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serialize_profile(profile)

    return Response(profile)


# UPDATE
@api_view(["PUT"])
def update_profile(request, student_id):

    result = db.student_profile.update_one(
        {"student_id": student_id},
        {"$set": request.data}
    )

    if result.matched_count == 0:
        return Response(
            {"message": "Student profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "message": "Student profile updated successfully"
    })


# DELETE
@api_view(["DELETE"])
def delete_profile(request, student_id):

    result = db.student_profile.delete_one({
        "student_id": student_id
    })

    if result.deleted_count == 0:
        return Response(
            {"message": "Student profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "message": "Student profile deleted successfully"
    })
