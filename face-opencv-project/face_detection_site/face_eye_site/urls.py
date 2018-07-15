from django.urls import path

from . import views

urlpatterns = [

    path('', views.homeFace, name='homeFace'),
    path('uimage/', views.uimage, name='uimage'),
    path('dface/', views.dface, name='dface'),
]
