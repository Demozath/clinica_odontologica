from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro_llamadas/', views.registro_llamadas_view, name='registro_llamadas'),
    path('totales_llamadas/', views.total_llamadas_supervisor, name='totales_llamadas')
    
]
