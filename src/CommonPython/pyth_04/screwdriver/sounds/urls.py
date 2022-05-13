from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sound/<uuid:pk>/renew', views.SoundGetForm, name='sound_source')
]