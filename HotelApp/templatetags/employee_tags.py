from django import template

from HotelApp.employee_display import display_department, display_gender

register = template.Library()


@register.filter
def department_vi(value):
    return display_department(value)


@register.filter
def gender_vi(value):
    return display_gender(value)
