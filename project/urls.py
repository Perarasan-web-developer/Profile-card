from django.urls import path
from . import views


urlpatterns = [
    path('',views.add,name='add'),
    path('abc/<str:a>/',views.abc,name="abc"),
    path('create-project',views.createProject,name="create-project"),
    path('update-project/<str:up>/',views.updateProject,name='updateproject'),
    path('delete-project/<str:dp>/',views.deleteProject,name='deleteproject'),
]