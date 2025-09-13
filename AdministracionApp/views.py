from django.shortcuts import render
from django.db import connection
from datetime import datetime

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("EXEC JO_sp_ListarVenta %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s", 
                       [1, 0, 0, 0, datetime.now(), datetime.now(), 0, 0, 'TIENDA VIRREY 1', '', 0, 0, ''])  # Reemplaza 'SomeTable' con el nombre real de tu tabla
        rows = cursor.fetchall()
    return render(request, 'index.html',{'rows': rows})

