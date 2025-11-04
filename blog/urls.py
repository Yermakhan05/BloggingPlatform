from django.urls import path

from blog.views import post_list, post_view, post_form, post_delete, post_update

urlpatterns = [
    path('', post_list, name='home'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>', post_view, name='post_detail'),
    path('posts/form/', post_form, name='post_form'),
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
    path('posts/<int:pk>/update/', post_update, name='post_update'),

]
