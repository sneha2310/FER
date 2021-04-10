from django.urls import path
from . import views
urlpatterns=[
    path('tech/', views.tech, name='technology')
]