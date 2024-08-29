from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.core.application.dtos.user_dtos import RegisterUserRequestDto

class RegisterUserView(APIView):

    def post(self, request):
        serializer = RegisterUserRequestDto(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
