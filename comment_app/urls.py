from django.contrib import admin
from django.urls import path
from comment_app import views
from django.views.generic import TemplateView

app_name = 'comments'

urlpatterns = [
    path('', TemplateView.as_view(template_name='comment/comment.html'), name='index'),
    path('commentit/', views.comments.as_view(), name='commentit'),
]
