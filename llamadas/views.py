from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LlamadaForm
from django.contrib.auth.decorators import login_required
from .models import Llamada
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from .models import Llamada



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('registro_llamadas')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecta')
    return render(request, 'llamadas/login.html')


@login_required
def registro_llamadas_view(request):
    if request.method == 'POST':
        form = LlamadaForm(request.POST)
        if form.is_valid():
            llamada = form.save(commit=False)
            llamada.asistente = request.user
            llamada.save()
            return redirect('registro_llamadas')
    else:
        form = LlamadaForm()
    llamadas = Llamada.objects.filter(asistente=request.user).order_by('-hora')
    return render(request, 'llamadas/registro_llamadas.html', {'form': form, 'llamadas': llamadas})


def is_supervisor(user):
    return user.groups.filter(name='SUPERVISOR').exists()

@user_passes_test(is_supervisor)
def total_llamadas_supervisor(request):
    totales_raw = Llamada.objects.values('asistente__username', 'resultado').annotate(total=Count('resultado')).order_by('-asistente', '-total')
    totales = [
        {
            'asistente': total['asistente__username'],
            'nombre': Llamada.RESULTADO_NOMBRES[total['resultado']],
            'total': total['total']
        }
        for total in totales_raw
    ]
    
    context = {
        'totales': totales,
    }
    
    return render(request, 'llamadas/totales_llamadas.html', context)
