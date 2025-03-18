from django.contrib import admin
from django.urls import path

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Read(전체)
    path('posts/', views.index),

    # Read(1)
    path('posts/<int:id>/', views.detail),
    # posts/ 뒤에 뭐가 들어오든 views.detail로 연결

    # create
    path('posts/new/', views.new),
    path('posts/create/', views.create),

    # delete
    path('posts/<int:id>/delete/', views.delete),

    # update
    path('posts/<int:id>/edit/', views.edit),
    path('posts/<int:id>/update/', views.update),
]
