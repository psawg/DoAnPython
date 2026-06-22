from django.shortcuts import render
from HotelApp import models


def dashboard_v2(request):
    total_booking = (
        models.Online_Booking.objects.count() +
        models.Offline_Booking.objects.count()
    )

    total_rooms = models.Add_Room.objects.count()

    total_employees = models.Add_Employee.objects.count()

    room_available = total_rooms

    context = {
        "total_booking": total_booking,
        "total_rooms": total_rooms,
        "total_employees": total_employees,
        "room_available": room_available,
    }

    return render(
        request,
        "dashboard/dashboard_v2.html",
        context
    )