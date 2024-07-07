from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('studio/', views.StudioList.as_view()),
    path('studio/<int:pk>/', views.StudioDetail.as_view()),
    path('photographer/', views.PhotographerList.as_view()),
    path('photographer/<int:pk>/', views.PhotographerDetail.as_view()),
    path('photoshoot/', views.PhotoshootList.as_view()),
    path('photoshoot/<int:pk>/', views.PhotoshootDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)