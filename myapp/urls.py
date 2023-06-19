from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("about/",views.about),
    path("categoria/", views.category),
    path("hello/<str:username>",views.hello),
    path("categorias/<int:id>",views.categorias),
    path("proyects",views.proyects),
    path("tasks/<int:id>",views.TasksList),
    
]