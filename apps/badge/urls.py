from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.getlist, name="list"),
    path('expand/', views.expand, name="expand"),
    path('list_bank/', views.consulta, name="list_bank"),
]
