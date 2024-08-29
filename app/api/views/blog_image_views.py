from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from app.core.application.services.blog_image_services import BlogImageService
from app.core.application.dtos.blog_image_dtos import BlogImageResponseDto
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UploadBlogImageView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('file_name', openapi.IN_FORM, description="File name of the image", type=openapi.TYPE_STRING),
            openapi.Parameter('title_name', openapi.IN_FORM, description="Title of the image", type=openapi.TYPE_STRING),
            openapi.Parameter('image_file', openapi.IN_FORM, description="Image file to upload", type=openapi.TYPE_FILE)
        ],
        responses={201: BlogImageResponseDto(), 400: openapi.Response(description="Invalid input or no image provided")}
    )
    def post(self, request):
        if getattr(self, 'swagger_fake_view', False):
            return None

        file_name = request.data.get('file_name')
        title = request.data.get('title_name')
        image_file = request.FILES.get('image_file')

        if not image_file:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        result = BlogImageService.upload_image(file_name, title, image_file)
        
        return Response(result, status=status.HTTP_201_CREATED)

class BlogImageListView(generics.ListAPIView):
    serializer_class = BlogImageResponseDto
    @swagger_auto_schema(
        responses={200: BlogImageResponseDto(many=True)}
    )
    def get(self, request):
        if getattr(self, 'swagger_fake_view', False):
            return None

        result = BlogImageService.get_all()
        return Response(result, status=status.HTTP_200_OK)