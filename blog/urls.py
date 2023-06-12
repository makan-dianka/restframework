from django.urls import path
from .views import (
    blog_list, blog_create,
    blog_update, blog_item,
    blog_delete
)


app_name='blog'
urlpatterns = [
    path('', blog_list.blog_list, name='blog_list'),
    path('create', blog_create.blog_create, name='blog_create'),
    path('update/<int:id>', blog_update.blog_update, name='blog_update'),
    path('delete/<int:id>', blog_delete.blog_delete, name='blog_delete'),
    path('<int:id>', blog_item.blog_item, name='blog_item'),
]