from rest_framework import generics, status
from rest_framework.response import Response
from app.core.application.services.blog_post_services import BlogPostService
from rest_framework.exceptions import ValidationError
from app.core.application.dtos.blog_post_dtos import BlogPostResponseDto, CreateBlogPostRequestDto, UpdateBlogPostRequestDto
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostResponseDto

    @swagger_auto_schema(
        responses={200: BlogPostResponseDto()}
    )
    def get(self, request, id):
        result = BlogPostService.get_by_id(id)
        return Response(result, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UpdateBlogPostRequestDto,
        responses={200: BlogPostResponseDto(), 400: 'Validation error'}
    )
    def put(self, request, id):
        try:
            result = BlogPostService.update(id=id, update_data=request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={200: BlogPostResponseDto()}
    )
    def delete(self, request, id):
        result = BlogPostService.delete(id)
        return Response(result, status=status.HTTP_200_OK)


class BlogPostCreateView(generics.CreateAPIView):
    serializer_class = BlogPostResponseDto

    @swagger_auto_schema(
        request_body=CreateBlogPostRequestDto,
        responses={201: BlogPostResponseDto(), 400: 'Validation error'}
    )
    def post(self, request):
        try:
            result = BlogPostService.create(data=request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostResponseDto

    @swagger_auto_schema(
        responses={200: BlogPostResponseDto(many=True)}
    )
    def get(self, request):
        result = BlogPostService.get_all()
        return Response(result, status=status.HTTP_200_OK)


class BlogPostUrlHandleView(generics.RetrieveAPIView):
    serializer_class = BlogPostResponseDto

    @swagger_auto_schema(
        responses={200: BlogPostResponseDto()}
    )
    def get(self, request, url_handle):
        print(url_handle)
        result = BlogPostService.get_by_url_handle(url_handle=url_handle)
        return Response(result, status=status.HTTP_200_OK)


class BlogPostCountView(generics.GenericAPIView):
    serializer_class = BlogPostResponseDto

    @swagger_auto_schema(
        responses={200: openapi.Response('Count of blog posts', schema=openapi.Schema(type=openapi.TYPE_INTEGER))}
    )
    def get(self, request):
        result = BlogPostService.get_count()
        return Response({"count": result}, status=status.HTTP_200_OK)
