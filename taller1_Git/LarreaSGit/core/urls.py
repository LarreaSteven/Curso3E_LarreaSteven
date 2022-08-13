from django.urls import path
from . import views
urlpatterns = [


path('', views.gitgit, name='core'),

#------HERENCIA-----#
path('hijo', views.hijo, name='hijo'),
]