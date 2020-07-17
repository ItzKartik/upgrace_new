from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('followers/', include('follow_app.urls')),
    path('likes/', include('like_app.urls')),
    path('comments/', include('comment_app.urls')),
    path('hashtags/', include('hashtag_app.urls')),
    url(r'^admin/', admin.site.urls),

    path('contact_us/', TemplateView.as_view(template_name="contact.html") ,name="contact_us"),
    path('how_it_works/', TemplateView.as_view(template_name="how_it_works.html") ,name="how_it_works"),
    path('about_us/', TemplateView.as_view(template_name="about.html") ,name="about_us"),
    path('', TemplateView.as_view(template_name="index.html") ,name="index"),
]
