from django.db import models
from django.contrib.auth.models import User

class Llamada(models.Model):
    OPCIONES_RESULTADO = [
        ('cita', 'Cita'),
        ('nocom', 'No se logra comunicación'),
        ('noint', 'No interesado'),
        ('dev', 'Paciente llama de vuelta'),
    ]
    asistente = models.ForeignKey(User, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=5, choices=OPCIONES_RESULTADO)
    comentarios = models.TextField(blank=True)
    
    RESULTADO_NOMBRES = dict(OPCIONES_RESULTADO)
    
    


