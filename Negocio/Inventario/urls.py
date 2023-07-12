from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.index,name="index"), 
    path('<int:id>', views.view_producto, name='view_producto'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edita, name='edit'),
    path('eliminar/<int:id>/', views.elimina, name='eliminar'),
    path('register/', views.registrar, name='register'),
    path('login/', LoginView.as_view(template_name='Inventario/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='Inventario/logout.html'),name='logout'),
    

]