from django.urls import path
from .views import Palindromo

urlpatterns = [

    path('palindromo/',Palindromo.as_view(),name='palindromo'),

]