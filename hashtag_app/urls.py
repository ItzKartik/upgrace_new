from django.contrib import admin
from django.urls import path
from hashtag_app import views
from django.views.generic import TemplateView

app_name = 'hashtags'

urlpatterns = [
    path('', TemplateView.as_view(template_name='hashtag/hashtag.html'), name='index'),
    path("fetch_hashtags/", views.generator.as_view(), name="generator")
]