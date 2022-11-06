from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', by_category, name='by_category'),
    path('story/<int:story_id>/', read_more, name='read_more'),
]
