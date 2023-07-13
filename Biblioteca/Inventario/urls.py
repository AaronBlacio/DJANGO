from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>', views.view_producto, name='view_producto'),
]