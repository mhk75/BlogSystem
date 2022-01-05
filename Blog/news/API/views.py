import datetime
from rest_framework import generics, status, filters
from news.API.serializers import NewsSerializer, CategorySerializer, CategorySearchSerializer
from news.models import News, Category
from rest_framework.response import Response


class GetNewsAPI(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()


class DeleteNewsAPI(generics.DestroyAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()


class CreateNewsAPI(generics.CreateAPIView):
    serializer_class = NewsSerializer

    def create(self, request, *args, **kwargs):
        try:
            cat_list = []
            for cat_id in request.data['categories']:
                cat_object = Category.objects.get(pk=cat_id)
                cat_list.append(cat_object)
        except Category.DoesNotExist:
            return Response({"message": "cant find category"}, status=status.HTTP_404_NOT_FOUND)
        try:
            News.objects.get(title=request.data['title'], content=request.data['content'])
            return Response({"message": "object already exist"}, status=status.HTTP_400_BAD_REQUEST)
        except News.DoesNotExist:
            new_obj = News.objects.create(title=request.data['title'], content=request.data['content'],
                                          created_at=datetime.datetime.now())
            new_obj.category.set(cat_list)
            return Response({"message": "object created successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "could not create cat object"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateNewsAPI(generics.UpdateAPIView):
    serializer_class = NewsSerializer

    def put(self, request, pk, *args, **kwargs):
        try:
            new_obj = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"message": "cant find new"}, status=status.HTTP_404_NOT_FOUND)
        if 'categories' in request.data:
            try:
                cat_list = []
                for cat_id in request.data['categories']:
                    cat_object = Category.objects.get(pk=cat_id)
                    cat_list.append(cat_object)
            except Category.DoesNotExist:
                return Response({"message": "cant find category"}, status=status.HTTP_404_NOT_FOUND)
            try:
                new_obj.category.set(cat_list)
            except:
                return Response({"message": "could not set category list"}, status=status.HTTP_400_BAD_REQUEST)
        if 'title' in request.data:
            try:
                new_obj.title = request.data['title']
            except:
                return Response({"message": "could not change title"}, status=status.HTTP_400_BAD_REQUEST)
        if 'content' in request.data:
            try:
                new_obj.content = request.data['content']
            except:
                return Response({"message": "could not change title"}, status=status.HTTP_400_BAD_REQUEST)
        new_obj.save()
        return Response({"message": "new updated successfully"}, status=status.HTTP_200_OK)


class NewsSearchAPI(generics.ListAPIView):
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        return News.objects.all()


class GetCategoriesAPI(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
        #return Category.objects.filter(level=0)


class DeleteCategoryAPI(generics.DestroyAPIView):
    serializer_class = CategorySerializer

    def delete(self, request, pk, *args, **kwargs):
        try:
            cat = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"message": "cant find category"}, status=status.HTTP_404_NOT_FOUND)

        if cat.children.first() is not None:
            return Response({"message": "cant remove category with sub category"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            cat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CreateCategoryAPI(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CreateChildCategoryAPI(generics.CreateAPIView):
    serializer_class = CategorySerializer

    def create(self, request, pk, *args, **kwargs):
        try:
            parent_cat = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"message": "cant find category"}, status=status.HTTP_404_NOT_FOUND)
        try:
            Category.objects.get(title=request.data['title'], parent=parent_cat)
        except Category.DoesNotExist:
            Category.objects.create(title=request.data['title'], parent=parent_cat)
            return Response({"message": "category created successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "could not create cat object"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategoryAPI(generics.UpdateAPIView):
    serializer_class = CategorySerializer

    def update(self, request, pk, *args, **kwargs):
        try:
            cat = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"message": "cant find category"}, status=status.HTTP_404_NOT_FOUND)
        try:
            cat.title = request.data['title']
            cat.parent = cat.parent
            cat.save()
            return Response({"message": "category updated successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "could not update cat object"}, status=status.HTTP_400_BAD_REQUEST)



