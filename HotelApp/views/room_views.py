from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from HotelApp import models
from HotelApp.forms import Add_Room_form
from HotelApp.room_display import ROOM_FLOOR_CHOICES, ROOM_TYPE_CHOICES
from django.http import JsonResponse

def _room_form_context(**extra):
    context = {
        'room_type_choices': ROOM_TYPE_CHOICES,
        'room_floor_choices': ROOM_FLOOR_CHOICES,
    }
    context.update(extra)
    return context


def _strip_post(request, key):
    return (request.POST.get(key) or '').strip()


def _parse_display_count(raw):
    if raw in (None, ''):
        return None
    try:
        count = int(raw)
    except (TypeError, ValueError):
        return None
    return count if count > 0 else None


def _all_rooms_queryset(search=None, limit=None):
    data = models.Add_Room.objects.all().order_by('-Id')

    if search:
        data = data.filter(
            Q(Room_Number__icontains=search)
            | Q(Room_Type__icontains=search)
            | Q(Room_Floor__icontains=search)
        )

    if limit:
        return data[:limit]

    return data


def Add_room(request):
    if request.method == 'POST':
        upload_image = request.FILES.get(
            'Room_Image'
        )

        room_number = _strip_post(request, 'Room_Number')
        room_type = _strip_post(request, 'Room_Type')
        room_floor = _strip_post(request, 'Room_Floor')

        if not room_number:
            data = models.Add_Room.objects.all().order_by('-Room_Number')
            return render(
                request,
                'admin/AddRoom.html',
                _room_form_context(
                    data=data,
                    error='Vui lòng nhập số phòng',
                ),
            )

        if not room_type:
            data = models.Add_Room.objects.all().order_by('-Room_Number')
            return render(
                request,
                'admin/AddRoom.html',
                _room_form_context(
                    data=data,
                    error='Vui lòng chọn loại phòng',
                ),
            )

        if not room_floor:
            data = models.Add_Room.objects.all().order_by('-Room_Number')
            return render(
                request,
                'admin/AddRoom.html',
                _room_form_context(
                    data=data,
                    error='Vui lòng chọn tầng phòng',
                ),
            )

        if models.Add_Room.objects.filter(Room_Number=room_number).exists():
            data = models.Add_Room.objects.all().order_by('-Room_Number')
            return render(
                request,
                'admin/AddRoom.html',
                _room_form_context(
                    data=data,
                    error='Số phòng đã tồn tại',
                ),
            )

        Data = models.Add_Room()
        Data.Room_Number = room_number
        Data.Room_Type = room_type
        Data.Room_Floor = room_floor
        Data.Room_Status = request.POST.get('Room_Status')
        Data.Room_Facility = _strip_post(request, 'Room_Facility')
        Data.Room_Price = _strip_post(request, 'Room_Price')
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
        _room_form_context(data=data),
    )


def Add_Room_Search(request):

    action = request.POST.get('action')

    # ===== HIỂN THỊ TẤT CẢ =====
    if action == 'all':
        return redirect('Add_room')

    # ===== SEARCH =====
    if action == 'search':
        search = (request.POST.get('serch') or '').strip()

        data = models.Add_Room.objects.all()

        if search:
            data = data.filter(
                Q(Room_Number__icontains=search)
                | Q(Room_Type__icontains=search)
                | Q(Room_Floor__icontains=search)
            )

        data = data.order_by('-Id')

        return render(
            request,
            'admin/AddRoom.html',
            {'data': data},
        )

    return redirect('Add_room')


def AddRooms_Delete(request, id):
    data = models.Add_Room.objects.get(Id=id)

    data.delete()

    return redirect('Add_room')

# def EditRooms(request, id):
#     data = models.Add_Room.objects.get(Id=id)
#     return HttpResponse(data.Room_Number)

def _edit_rooms_context(room, error=None):
    return _room_form_context(
        data=room,
        rooms=models.Add_Room.objects.all().order_by('-Id'),
        error=error,
    )


def EditRooms(request, id):
    data = models.Add_Room.objects.get(Id=id)

    if request.method == 'POST':
        room_number = _strip_post(request, 'Room_Number')
        room_floor = _strip_post(request, 'Room_Floor')
        room_type = _strip_post(request, 'Room_Type')

        if not room_number:
            return render(
                request,
                'admin/EditRooms.html',
                _edit_rooms_context(data, 'Vui lòng nhập số phòng'),
            )

        if not room_floor:
            return render(
                request,
                'admin/EditRooms.html',
                _edit_rooms_context(data, 'Vui lòng chọn tầng phòng'),
            )

        if not room_type:
            return render(
                request,
                'admin/EditRooms.html',
                _edit_rooms_context(data, 'Vui lòng chọn loại phòng'),
            )

        if (
            room_number != data.Room_Number
            and models.Add_Room.objects.filter(
                Room_Number=room_number
            ).exists()
        ):
            return render(
                request,
                'admin/EditRooms.html',
                _edit_rooms_context(data, 'Số phòng đã tồn tại'),
            )

        data.Room_Number = room_number
        data.Room_Type = room_type
        data.Room_Floor = room_floor
        data.Room_Facility = request.POST.get('Room_Facility')
        data.Room_Price = request.POST.get('Room_Price')
        data.Room_Status = request.POST.get('Room_Status')

        upload_image = request.FILES.get('Room_Image')
        if upload_image:
            data.Room_Image = upload_image

        data.save()
        return redirect('Add_room')

    return render(
        request,
        'admin/EditRooms.html',
        _edit_rooms_context(data),
    )


def All_Room(request):
    display_count = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'all':
            return redirect('All_Room')

        search = (request.POST.get('search') or '').strip()
        display_count = request.POST.get('display_count', '')
        limit = _parse_display_count(display_count)

        data = _all_rooms_queryset(search=search, limit=limit)

        return render(
            request,
            'admin/AllRooms.html',
            {
                'data': data,
                'display_count': display_count,
                'search': search,
            },
        )

    data = _all_rooms_queryset()

    return render(
        request,
        'admin/AllRooms.html',
        {'data': data},
    )


def AllRooms_Delete(request, id):
    data = models.Add_Room.objects.get(Id=id)

    data.delete()

    return redirect('All_Room')


def check_availability(request):

    rooms = models.Add_Room.objects.all().order_by('Room_Number')

    return render(
        request,
        'room_rows.html',
        {
            'rooms': rooms
        }
    )


def room_detail_api(request, room_id):

    room = models.Add_Room.objects.get(Id=room_id)

    return JsonResponse({
        'room_number': room.Room_Number,
        'room_type': room.Room_Type,
        'room_floor': room.Room_Floor,
        'room_price': room.Room_Price,
        'room_image': room.Room_Image.url
    })