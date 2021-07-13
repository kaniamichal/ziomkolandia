from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('atrakcje/', views.atractions, name='atrakcje'),
    path('atrakcje/CrashKader', views.crash_kader, name='CrashKader'),
    path('atrakcje/CrashRunner', views.crash_runner, name='CrashRunner'),
    path('atrakcje/KlockiMaxi', views.klocki_maxi, name='KlockiMaxi'),
    path('atrakcje/ArcheryTag', views.archery_tag, name='ArcheryTag'),
    path('atrakcje/BumperBall', views.bumper_ball, name='BumperBall'),
    path('atrakcje/ZjezdzalniaKlocki', views.zjazd_klocki, name='ZjazdKolcki'),
    path('atrakcje/ClimbingWall', views.climbing_wall, name='ClimbingWall'),
    path('atrakcje/DmuchanieCklocki', views.dmuchaniec_klocki, name='DmuchaniecKlocki'),
    path('atrakcje/SkakaniecKlocki', views.skakaniec_klocki, name='SkakaniecKlocki'),
    path('atrakcje/PoduchaWodna', views.poducha_wodna, name='PoduchaWodna'),
    path('atrakcje/Motorowka', views.motorowka, name='Motorowka'),
    path('eventy/', views.eventy, name='eventy'),
    path('oferta/', views.offer, name='oferta'),
    path('obozy/', views.camps, name='obozy'),
    path('przedszkola/', views.przedszkola, name='przedszkola'),
    path('przedszkola-zapisy/', views.kids_enroll, name='kids_enroll'),
    path('oboz-zapisy/', views.kids_enroll_camp, name='kids_enroll_camp'),
    path('polkolonie-zapisy/', views.kids_enroll_day_camp, name ='kids_enroll_day_camp'),
    path('thanks/', views.thanks, name='thanks'),
    path('contact/', views.contact_form, name='contact'),
    path('zielona-szkola/', views.green, name='zielona-szkola'),
    path('oferta-zielona-szkola/', views.offer_green, name='oferta-zielona-szkola'),
    path('zielona-szkola/ziomkolandia-mini', views.green_mini, name='ziomkolandia-mini'),
    path('zielona-szkola/ziomkolandia-maxi', views.green_maxi, name='ziomkolandia-maxi'),
    path('zielona-szkola/ziomkolandia-xl', views.green_xl, name='ziomkolandia-xl'),
    path('captcha/', include('captcha.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

