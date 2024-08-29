from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from app.core.application.services.blog_image_services import BlogImageService

class UploadBlogImageView(APIView):

    def post(self, request):
        file_name = request.data.get('file_name')
        title = request.data.get('title_name')
        image_file = request.FILES.get('image_file')

        if not image_file:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        result = BlogImageService.upload_image(file_name, title, image_file)
        
        return Response(result, status=status.HTTP_201_CREATED)

class BlogImageListView(generics.ListAPIView):
    
    def get(self, request):
        result = BlogImageService.get_all()
        return Response(result, status=status.HTTP_200_OK)