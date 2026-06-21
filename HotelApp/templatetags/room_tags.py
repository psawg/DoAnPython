from django import template

from HotelApp.room_display import display_room_floor, display_room_type

register = template.Library()


@register.filter
def room_type_vi(value):
    return display_room_type(value)


@register.filter
def room_floor_vi(value):
    return display_room_floor(value)
