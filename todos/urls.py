from django.urls import path
from .views import index, search, todo_list_view


urlpatterns = [
    path('', index, name='index'),
    path('list', todo_list_view, name='list'),
    path('search/', search, name='search')
]
