from rest_framework import generics, status
from rest_framework.response import Response
from app.core.application.services.blog_post_services import BlogPostService
from rest_framework.exceptions import ValidationError

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, id):
        result = BlogPostService.get_by_id(id)
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            result = BlogPostService.update(id=id, update_data=request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = BlogPostService.delete(id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)


class BlogPostCreateView(generics.CreateAPIView):
    def post(self, request):
        try:
            result = BlogPostService.create(data=request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BlogPostListView(generics.ListAPIView):
    def get(self, request):
        result = BlogPostService.get_all()
        return Response(result, status=status.HTTP_200_OK)


class BlogPostUrlHandleView(generics.RetrieveAPIView):
    def get(self, request, url_handle):
        print(url_handle)
        result = BlogPostService.get_by_url_handle(url_handle=url_handle)
        return Response(result, status=status.HTTP_200_OK)


class BlogPostCountView(generics.GenericAPIView):
    def get(self, request):
        result = BlogPostService.get_count()
        return Response({"count": result}, status=status.HTTP_200_OK)
