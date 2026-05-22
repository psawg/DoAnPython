from django.shortcuts import render, redirect
from django.http import HttpResponse

from HotelApp import models
from HotelApp.forms import (
    Online_Booking_form,
    offline_Booking_form
)


def OnlineBooking(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Img')

        MyData = models.Online_Booking()

        MyData.Id = request.POST.get('Id')
        MyData.Check_in = request.POST.get('Check_in')
        MyData.Check_out = request.POST.get('Check_out')
        MyData.ADULT = request.POST.get('ADULT')
        MyData.CHILDREN = request.POST.get('CHILDREN')
        MyData.Name = request.POST.get('Name')
        MyData.Surname = request.POST.get('Surname')
        MyData.Email = request.POST.get('Email')
        MyData.Phone_Number = request.POST.get('Phone_Number')
        MyData.Nid_No = request.POST.get('Nid_No')
        MyData.City = request.POST.get('City')
        MyData.Country = request.POST.get('Country')
        MyData.Img = upload_image
        MyData.Address = request.POST.get('Address')
        MyData.Date = request.POST.get('Date')
        MyData.Time = request.POST.get('Time')

        MyData.save()

        return HttpResponse('Booking Successfully')

    return render(request, 'online_booking_page.html')


def online_Booking_info(request):
    if request.method == 'POST':
        search = request.POST.get('search')

        show = (
            models.Online_Booking.objects.filter(Country=search)
            or
            models.Online_Booking.objects.filter(Name=search)
        )

        return render(
            request,
            'admin/Online_Booking.html',
            {"data": show}
        )

    data = models.Online_Booking.objects.all().order_by('-Id')

    return render(
        request,
        'admin/Online_Booking.html',
        {'data': data}
    )


def Edit_online_Booking(request, id):
    data = models.Online_Booking.objects.get(Id=id)

    if request.method == 'POST':
        form = Online_Booking_form(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():
            form.save()
            return redirect('online_Booking_info')

        return HttpResponse("Failed")

    return render(
        request,
        'admin/EditonlineBooking.html',
        {'data': data}
    )


def AddCustomer(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Upload_Image')

        Data = models.Offline_Booking()

        Data.Customer_Id = request.POST.get('Customer_Id')
        Data.Check_in = request.POST.get('Check_in')
        Data.Check_out = request.POST.get('Check_out')
        Data.First_Name = request.POST.get('First_Name')
        Data.Last_Name = request.POST.get('Last_Name')
        Data.Email = request.POST.get('Email')
        Data.Mobile_Number = request.POST.get('Mobile_Number')
        Data.ADULT = request.POST.get('ADULT')
        Data.CHILDREN = request.POST.get('CHILDREN')
        Data.Total_Person = request.POST.get('Total_Person')
        Data.Select_Room = request.POST.get('Select_Room')
        Data.Room_Number = request.POST.get('Room_Number')
        Data.Gender = request.POST.get('Gender')
        Data.Personal_Identity = request.POST.get('Personal_Identity')
        Data.Upload_Image = upload_image
        Data.Country = request.POST.get('Country')
        Data.Address = request.POST.get('Address')
        Data.Date = request.POST.get('Date')
        Data.Time = request.POST.get('Time')

        Data.save()

        return redirect('AddCustomer')

    data = models.Offline_Booking.objects.all().order_by('-Customer_Id')

    return render(
        request,
        'admin/AddCustomer.html',
        {'data': data}
    )


def AllCustomer(request):
    if request.method == 'POST':
        search = request.POST.get('search')

        data = (
            models.Offline_Booking.objects.filter(
                First_Name=search
            )
            or
            models.Offline_Booking.objects.filter(
                Email=search
            )
        )

        return render(
            request,
            'admin/AllCustomer.html',
            {"data": data}
        )

    data = models.Offline_Booking.objects.all().order_by(
        '-Customer_Id'
    )

    return render(
        request,
        'admin/AllCustomer.html',
        {'data': data}
    )


def EditCustomer(request, id):
    data = models.Offline_Booking.objects.get(
        Customer_Id=id
    )

    if request.method == 'POST':
        form = offline_Booking_form(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():
            form.save()
            return redirect('AllCustomer')

        return HttpResponse("Failed")

    return render(
        request,
        'admin/EditCustomer.html',
        {'data': data}
    )


def Delete(request, id):
    data = models.Online_Booking.objects.get(Id=id)
    data.delete()

    return redirect('online_Booking_info')


def Search(request):
    if request.method == 'POST':
        search = request.POST.get('serch')

        data = (
            models.Offline_Booking.objects.filter(
                First_Name=search
            )
            or
            models.Offline_Booking.objects.filter(
                Email=search
            )
        )

        return render(
            request,
            'admin/AddCustomer.html',
            {"data": data}
        )


def AddCustpage_Delete(request, id):
    data = models.Offline_Booking.objects.get(
        Customer_Id=id
    )

    data.delete()

    return redirect('AddCustomer')


def AllCustpage_Delete(request, id):
    data = models.Offline_Booking.objects.get(
        Customer_Id=id
    )

    data.delete()

    return redirect('AllCustomer')