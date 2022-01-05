from django.urls import path
from news.API.views import *

urlpatterns =[
    path('news/list/', GetNewsAPI.as_view()),
    path('news/delete/<int:pk>/', DeleteNewsAPI.as_view()),
    path('news/submit/', CreateNewsAPI.as_view()),
    path('news/update/<int:pk>/', UpdateNewsAPI.as_view()),
    path('news/search/', NewsSearchAPI.as_view()),
    path('category/list/', GetCategoriesAPI.as_view()),
    path('category/delete/<int:pk>/', DeleteCategoryAPI.as_view()),
    path('category/submit/', CreateCategoryAPI.as_view()),
    path('category/submit/<int:pk>', CreateChildCategoryAPI.as_view()),
    path('category/update/<int:pk>', UpdateCategoryAPI.as_view()),
]
