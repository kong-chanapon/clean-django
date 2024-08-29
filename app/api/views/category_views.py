from rest_framework import generics, status
from rest_framework.response import Response
from app.core.application.services.category_services import CategoryService
from rest_framework.exceptions import ValidationError
from app.core.application.dtos.category_dtos import CategoryResponseDto, CreateCategoryRequestDto, UpdateCategoryRequestDto
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryResponseDto

    @swagger_auto_schema(
        responses={200: CategoryResponseDto()}
    )
    def get(self, request, id):
        if getattr(self, 'swagger_fake_view', False):
            return None

        result = CategoryService.get_by_id(id)
        return Response(result, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=UpdateCategoryRequestDto,
        responses={200: CategoryResponseDto(), 400: 'Validation error'}
    )
    def put(self, request, id):
        
        try:
            result = CategoryService.update(id=id, update_data=request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={200: CategoryResponseDto()}
    )
    def delete(self, request, id):
        result = CategoryService.delete(id)
        return Response(result, status=status.HTTP_200_OK)
    



class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryResponseDto

    @swagger_auto_schema(
        request_body=CreateCategoryRequestDto,
        responses={201: CategoryResponseDto(), 400: 'Validation error'}
    )
    def post(self, request):
        try:
            result = CategoryService.create(data=request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryResponseDto

    @swagger_auto_schema(
        responses={200: CategoryResponseDto(many=True)}
    )
    def get(self, request):
        result = CategoryService.get_all()
        return Response(result, status=status.HTTP_200_OK)


class CategoryUrlHandleView(generics.RetrieveAPIView):
    serializer_class = CategoryResponseDto

    @swagger_auto_schema(
        responses={200: CategoryResponseDto()}
    )
    def get(self, request, url_handle):
        print(url_handle)
        result = CategoryService.get_by_url_handle(url_handle=url_handle)
        return Response(result, status=status.HTTP_200_OK)


class CategoryCountView(generics.GenericAPIView):
    serializer_class = CategoryResponseDto

    @swagger_auto_schema(
        responses={200: openapi.Response('Count of categories', schema=openapi.Schema(type=openapi.TYPE_INTEGER))}
    )
    def get(self, request):
        result = CategoryService.get_count()
        return Response({"count": result}, status=status.HTTP_200_OK)
