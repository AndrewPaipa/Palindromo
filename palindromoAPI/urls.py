from django.urls import path
from .views import Palindromo, Index

urlpatterns = [

    path('',Index.as_view(),name='index'),
    path('palindromo/',Palindromo.as_view(),name='palindromo'),

]