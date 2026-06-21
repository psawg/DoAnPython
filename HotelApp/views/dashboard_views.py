from django.http import HttpResponse
from django.shortcuts import render, redirect

from HotelApp import models


def Home(request):
    return render(request, 'Home.html')


def all(request):
    return render(request, 'allinclude.html')


def all_admin(request):
    return render(request, 'admin/AdminAllinclude.html')


def Admin(request):

    role = request.session.get('role')

    if role not in ['admin', 'employee']:
        return redirect('Aothur_login')

    data = models.Online_Booking.objects.all().order_by('-Id')

    return render(
        request,
        'admin/Admin.html',
        {
            'data': data,
            'username': request.session.get('user_name'),
            'role': role
        }
    )

def EmployeeShow(request):
    return render(request, 'admin/EmployeeShow.html')