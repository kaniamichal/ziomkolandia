from card_me.base import patterns
from django.conf.urls import include, url
import staticmedia
from django.urls import path

urlpatterns = [
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),
    ] + staticmedia.serve()
