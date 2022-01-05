from rest_framework import serializers
from news.models import Category, News


class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    category = serializers.SerializerMethodField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField()

    def get_category(self, obj):
        cat_list = []
        for category in obj.category.all():
            cat_list.append(category.title)
        return cat_list

    class Meta:
        model = News
        fields = ['id', 'title', 'category', 'content', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    #children = serializers.SerializerMethodField()

    class Meta:
        #depth = 1
        model = Category
        fields = ['id', 'title']

    def get_children(self, obj):
        return CategorySerializer(obj.get_children(), many=True).data


class CategorySearchSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = Category
        fields = ['id', 'title']