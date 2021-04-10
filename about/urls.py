from django.urls import path
from . import views
urlpatterns=[
    path('ab/', views.abouts, name='about')
]