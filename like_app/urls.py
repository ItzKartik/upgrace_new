from django.contrib import admin
from django.urls import path
from like_app import views
from django.views.generic import TemplateView

app_name = 'likes'

urlpatterns = [
    path('', TemplateView.as_view(template_name='like/like.html'), name='index'),
    path("likeit/", views.likes.as_view(), name="likeit")
]
