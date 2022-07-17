from django.urls import path
from .views import Roller


urlpatterns = [
    path('', Roller.as_view()),
]

