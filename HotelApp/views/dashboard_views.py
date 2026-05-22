from django.shortcuts import render

from HotelApp import models


def Home(request):
    return render(request, 'Home.html')


def all(request):
    return render(request, 'allinclude.html')


def all_admin(request):
    return render(request, 'admin/AdminAllinclude.html')


def Admin(request):
    data = models.Online_Booking.objects.all().order_by('-Id')

    return render(
        request,
        'admin/Admin.html',
        {'data': data}
    )


def EmployeeShow(request):
    return render(request, 'admin/EmployeeShow.html')