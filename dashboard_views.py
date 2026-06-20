from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Online_Booking, Offline_Booking, Add_Employee, Add_Room


def get_dashboard_stats():
    """Aggregate all stats needed for the dashboard."""
    total_online = Online_Booking.objects.count()
    total_offline = Offline_Booking.objects.count()
    total_bookings = total_online + total_offline

    total_rooms = Add_Room.objects.count()

    occupied_rooms = Offline_Booking.objects.values('Room_Number').distinct().count()
    available_rooms = max(total_rooms - occupied_rooms, 0)

    total_employees = Add_Employee.objects.count()

    recent_online = Online_Booking.objects.order_by('-Date', '-Time')[:5]
    recent_offline = Offline_Booking.objects.order_by('-Date', '-Time')[:5]

    rooms_by_type = (
        Add_Room.objects.values('Room_Type')
        .annotate(count=Count('Id'))
        .order_by('-count')
    )

    employees_by_dept = (
        Add_Employee.objects.values('Departments')
        .annotate(count=Count('Employee_Id'))
        .order_by('-count')
    )

    all_rooms = Add_Room.objects.all()
    booked_numbers = set(
        Offline_Booking.objects.values_list('Room_Number', flat=True)
    )
    room_status = []
    for room in all_rooms:
        status = 'occupied' if room.Room_Number in booked_numbers else 'available'
        room_status.append({
            'number': room.Room_Number,
            'type': room.Room_Type,
            'floor': room.Room_Floor,
            'price': room.Room_Price,
            'status': status,
        })

    return {
        'total_bookings': total_bookings,
        'total_online': total_online,
        'total_offline': total_offline,
        'total_rooms': total_rooms,
        'available_rooms': available_rooms,
        'occupied_rooms': occupied_rooms,
        'total_employees': total_employees,
        'recent_online': recent_online,
        'recent_offline': recent_offline,
        'rooms_by_type': list(rooms_by_type),
        'employees_by_dept': list(employees_by_dept),
        'room_status': room_status,
        'pending_online': total_online,
    }


def dashboard(request):
    if not request.session.get('Authority_Email'):
        return redirect('Aothur_login')
    stats = get_dashboard_stats()
    return render(request, 'HotelApp/dashboard.html', stats)
