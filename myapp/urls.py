from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('products', views.products),
    path('hello/<str:username>', views.hello),
    path('number/<int:numero>',views.number),
    path('projects',views.projects),
    path('tasks',views.tasks),
    path('create_task', views.create_task),
]
