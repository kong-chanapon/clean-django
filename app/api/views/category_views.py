from rest_framework import generics, status
from rest_framework.response import Response
from app.core.application.services.category_services import CategoryService
from rest_framework.exceptions import ValidationError

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, id):
        result = CategoryService.get_by_id(id)
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            result = CategoryService.update(id=id, update_data=request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = CategoryService.delete(id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)


class CategoryCreateView(generics.CreateAPIView):
    def post(self, request):
        try:
            result = CategoryService.create(data=request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(generics.ListAPIView):
    def get(self, request):
        result = CategoryService.get_all()
        return Response(result, status=status.HTTP_200_OK)


class CategoryUrlHandleView(generics.RetrieveAPIView):
    def get(self, request, url_handle):
        print(url_handle)
        result = CategoryService.get_by_url_handle(url_handle=url_handle)
        return Response(result, status=status.HTTP_200_OK)


class CategoryCountView(generics.GenericAPIView):
    def get(self, request):
        result = CategoryService.get_count()
        return Response({"count": result}, status=status.HTTP_200_OK)
