from django.shortcuts import render, redirect
from django.http import HttpResponse

from HotelApp import models
from HotelApp.forms import Add_Room_form


def Add_room(request):
    if request.method == 'POST':
        upload_image = request.FILES.get(
            'Room_Image'
        )

        Data = models.Add_Room()

        Data.Room_Number = request.POST.get(
            'Room_Number'
        )
        Data.Room_Type = request.POST.get(
            'Room_Type'
        )
        Data.Room_Floor = request.POST.get(
            'Room_Floor'
        )
        Data.Room_Facility = request.POST.get(
            'Room_Facility'
        )
        Data.Room_Price = request.POST.get(
            'Room_Price'
        )
        Data.Room_Image = upload_image
        Data.Date = request.POST.get('Date')
        Data.Time = request.POST.get('Time')

        Data.save()

        return redirect('Add_room')

    data = models.Add_Room.objects.all().order_by(
        '-Room_Number'
    )

    return render(
        request,
        'admin/AddRoom.html',
        {'data': data}
    )


def Add_Room_Search(request):
    if request.method == 'POST':

        action = request.POST.get('action')
        search = request.POST.get('serch')

        if action == 'showall':
            data = models.Add_Room.objects.all().order_by('-Id')

        else:
            data = (
                models.Add_Room.objects.filter(
                    Room_Number=search
                )
                or
                models.Add_Room.objects.filter(
                    Room_Type=search
                )
            ) 

        return render(
            request,
            'admin/AddRoom.html',
            {'data': data}
        )

def AddRooms_Delete(request, id):
    data = models.Add_Room.objects.get(Id=id)

    data.delete()

    return redirect('Add_room')


def EditRooms(request, id):
    data = models.Add_Room.objects.get(Id=id)

    if request.method == 'POST':
        form = Add_Room_form(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():
            form.save()
            return redirect('All_Room')

        return HttpResponse("Failed")

    return render(
        request,
        'admin/EditRooms.html',
        {'data': data}
    )


def All_Room(request):
    if request.method == 'POST':
        search = request.POST.get('search')

        data = (
            models.Add_Room.objects.filter(
                Room_Number=search
            )
            or
            models.Add_Room.objects.filter(
                Room_Type=search
            )
        )

        return render(
            request,
            'admin/AllRooms.html',
            {"data": data}
        )

    data = models.Add_Room.objects.all().order_by(
        '-Id'
    )

    return render(
        request,
        'admin/AllRooms.html',
        {'data': data}
    )


def AllRooms_Delete(request, id):
    data = models.Add_Room.objects.get(Id=id)

    data.delete()

    return redirect('All_Room')