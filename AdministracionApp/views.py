from django.shortcuts import render
from django.db import connection
from datetime import datetime

def paginaIndex(request):
    return render(request, 'index.html')

def iniciarsesion(request):
    if request.method == 'POST':
        #try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC JO_sp_ListarTrabajador %s, %s, %s",[
                    2,
                    request.POST['usuario'],
                    request.POST['password']
                ])
                filas = cursor.fetchall()
                if filas:
                    return render(request, 'ventas.html', {'filas': filas})
                else:
                    return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

def ventas(request):
    with connection.cursor() as cursor:
        cursor.execute("EXEC JO_sp_ListarVenta %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s", 
                       [1, 0, 0, 0, datetime.now(), datetime.now(), 0, 0, 'TIENDA VIRREY 2', '', 0, 0, ''])  # Reemplaza 'SomeTable' con el nombre real de tu tabla
        rows = cursor.fetchall()
    return render(request, 'ventas.html',{'rows': rows})
