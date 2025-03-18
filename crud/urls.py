from django.contrib import admin
from django.urls import path

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('posts/<int:id>/', views.detail),
    # posts/1/
    # posts/10/
    # posts/ 뒤에 뭐가 들어오든 views.detail로 연결
]
