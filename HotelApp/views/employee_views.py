from django.shortcuts import render, redirect
from django.http import HttpResponse

from HotelApp import models
from HotelApp.forms import (
    Add_Employee_form,
    Add_salary_form
)


def Addemployee(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Upload_Image')

        Data = models.Add_Employee()

        Data.Employee_Id = request.POST.get('Employee_Id')
        Data.First_Name = request.POST.get('First_Name')
        Data.Last_Name = request.POST.get('Last_Name')
        Data.Email = request.POST.get('Email')
        Data.Mobile_Number = request.POST.get('Mobile_Number')
        Data.Joining_Date = request.POST.get('Joining_Date')
        Data.Dateof_Birth = request.POST.get('Dateof_Birth')
        Data.Departments = request.POST.get('Departments')
        Data.Gender = request.POST.get('Gender')
        Data.Blood_Group = request.POST.get('Blood_Group')
        Data.Education = request.POST.get('Education')
        Data.Personal_Identity = request.POST.get('Personal_Identity')
        Data.Guardian = request.POST.get('Guardian')
        Data.Guardian_Number = request.POST.get('Guardian_Number')
        Data.Upload_Image = upload_image
        Data.Address = request.POST.get('Address')
        Data.Date = request.POST.get('Date')
        Data.Time = request.POST.get('Time')

        Data.save()

        return redirect('Addemployee')

    data = models.Add_Employee.objects.all().order_by(
        '-Employee_Id'
    )

    return render(
        request,
        'admin/addemployee.html',
        {'data': data}
    )


def Editemployee(request, id):
    data = models.Add_Employee.objects.get(
        Employee_Id=id
    )

    if request.method == 'POST':
        form = Add_Employee_form(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():
            form.save()
            return redirect('Allemployee')

        return HttpResponse("Failed")

    return render(
        request,
        'admin/Editemployee.html',
        {'data': data}
    )


def Allemployee(request):
    if request.method == 'POST':
        search = request.POST.get('search')

        data = (
            models.Add_Employee.objects.filter(
                Employee_Id=search
            )
            or
            models.Add_Employee.objects.filter(
                First_Name=search
            )
        )

        return render(
            request,
            'admin/allemployee.html',
            {"data": data}
        )

    data = models.Add_Employee.objects.all().order_by(
        '-Employee_Id'
    )

    return render(
        request,
        'admin/allemployee.html',
        {'data': data}
    )


def AddEmplopage_Delete(request, id):
    data = models.Add_Employee.objects.get(
        Employee_Id=id
    )

    data.delete()

    return redirect('Addemployee')


def Add_Employee_Search(request):
    if request.method == 'POST':
        search = request.POST.get('serch')

        data = (
            models.Add_Employee.objects.filter(
                Employee_Id=search
            )
            or
            models.Add_Employee.objects.filter(
                First_Name=search
            )
        )

        return render(
            request,
            'admin/addemployee.html',
            {"data": data}
        )


def AllEmployee_Delete(request, id):
    data = models.Add_Employee.objects.get(
        Employee_Id=id
    )

    data.delete()

    return redirect('Allemployee')


def AddEmployeeSalary(request):
    if request.method == 'POST':
        Data = models.Add_Salarys()

        Data.Employee_Id = request.POST.get(
            'Employee_Id'
        )
        Data.Employee_Name = request.POST.get(
            'Employee_Name'
        )
        Data.Email = request.POST.get('Email ')
        Data.Mobile_Number = request.POST.get(
            'Mobile_Number'
        )
        Data.Departments = request.POST.get(
            'Departments'
        )
        Data.Salary = request.POST.get('Salary')
        Data.Date = request.POST.get('Date')
        Data.Time = request.POST.get('Time')

        Data.save()

        return redirect('AddEmployeeSalary')

    return render(
        request,
        'admin/AddEmployeeSalary.html'
    )