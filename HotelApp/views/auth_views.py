from django.shortcuts import render, redirect
from django.http import HttpResponse
from HotelApp import models


def Aothur_login(request):

    # đã đăng nhập rồi thì vào dashboard luôn
    if (
            request.session.get('user_id')
            and
            request.session.get('role') in ['admin', 'employee']
    ):
        return redirect('Adminpage')

    if request.method == 'POST':

        User_email = request.POST.get('Email')
        User_password = request.POST.get('Password')

        remember_me = request.POST.get('remember_me')

        user = models.Authorregis.objects.filter(
            Email=User_email,
            Password=User_password
        ).first()

        if user:

            request.session['user_id'] = user.Id
            request.session['user_name'] = user.Fname
            request.session['role'] = user.Role

            # Remember Me
            if remember_me:
                request.session.set_expiry(1209600)  # 14 ngày
            else:
                request.session.set_expiry(0)  # đóng trình duyệt là mất

            return redirect('Adminpage')

        else:
            return HttpResponse(
                'Email hoặc Password không đúng'
            )

    return render(
        request,
        'Athur_login_page.html'
    )

def auth_logout(request):

    request.session.flush()

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


def is_admin(request):
    return request.session.get('role') == 'admin'


def is_employee(request):
    return request.session.get('role') == 'employee'


def is_staff(request):
    return request.session.get('role') in [
        'admin',
        'employee'
    ]