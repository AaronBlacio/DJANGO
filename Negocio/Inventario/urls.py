from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"), 
    path('<int:id>', views.view_producto, name='view_producto'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edita, name='edit'),
    path('eliminar/<int:id>/', views.elimina, name='eliminar'),
]