from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('router/<str:router>', views.routeTable, name='routeTable'),
    path('router/<str:router>/<str:intType>/<str:intId>', views.set_interface, name='set_interface'),
]
