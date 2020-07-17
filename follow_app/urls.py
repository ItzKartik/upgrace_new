from django.contrib import admin
from django.urls import path
from follow_app import views
from django.views.generic import TemplateView

app_name = 'followers'

urlpatterns = [
    path('', TemplateView.as_view(template_name='follower/follower.html'), name='index'),
    path("followthis/", views.followers.as_view(), name="followthis"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("join_us/", views.join_us, name="join_us")
]
