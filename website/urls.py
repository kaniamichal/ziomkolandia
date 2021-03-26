import captcha
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('przedszkola/', views.kids_enroll, name='kids_enroll'),
    path('oboz_zapis/', views.kids_enroll_camp, name='kids_enroll_camp'),
    path('thanks/', views.thanks, name='thanks'),
    path('captcha/', include('captcha.urls')),
]

