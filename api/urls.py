from django.urls import path

from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('project',views.getproject),
    path('project/<str:pk>',views.getprojectid)
]
