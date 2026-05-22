from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse

from HotelApp import models


def Aothur_login(request):
    if request.method == 'POST':
        User_email = request.POST.get('Email')
        User_password = request.POST.get('Password')

        if models.Authorregis.objects.filter(
            Email=User_email,
            Password=User_password
        ):
            return redirect("Adminpage")
        else:
            return HttpResponse('user name and password not matching')

    return render(request, 'Athur_login_page.html')


def auth_logout(request):
    logout(request)
    return redirect('Home')


def Aothur_Reg(request):
    if request.method == 'POST':
        Data = models.Authorregis()

        Data.Fname = request.POST.get('Fname')
        Data.Lname = request.POST.get('Lname')
        Data.Email = request.POST.get('Email')
        Data.Phone_Number = request.POST.get('Phone_Number')
        Data.Password = request.POST.get('Password')

        Con_password = request.POST.get('Con_password')

        if Data.Password == Con_password:
            Data.save()
            return redirect('Aothur_login')

        return HttpResponse(
            'password and confirm password not matching'
        )

    return render(request, 'Athur_Register_Page.html')


def Aothur_Fotpass(request):
    return render(request, 'Author_forgetpass_page.html')