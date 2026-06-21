from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="Home"),
    path('all', all),

    path(
        'OnlineBooking',
        OnlineBooking,
        name='OnlineBooking'
    ),

    path(
        'Aothur_login',
        Aothur_login,
        name='Aothur_login'
    ),

    path(
        'auth_logout',
        auth_logout,
        name='auth_logout'
    ),

    path(
        'Aothur_Reg',
        Aothur_Reg,
        name='Aothur_Reg'
    ),

    path(
        'Aothur_Fotpass',
        Aothur_Fotpass,
        name='Aothur_Fotpass'
    ),

    path('all_admin', all_admin),

    path(
        'Adminpage',
        Admin,
        name='Adminpage'
    ),

    path(
        'Addemployee',
        Addemployee,
        name='Addemployee'
    ),

    path(
        'Editemployee/<id>',
        Editemployee,
        name='Editemployee'
    ),

    path(
        'Allemployee',
        Allemployee,
        name='Allemployee'
    ),

    path(
        'online_Booking_info',
        online_Booking_info,
        name='online_Booking_info'
    ),

    path(
        'Edit_online_Booking/<id>',
        Edit_online_Booking,
        name='Edit_online_Booking'
    ),

    path(
        'AddCustomer',
        AddCustomer,
        name='AddCustomer'
    ),

    path(
        'AllCustomer',
        AllCustomer,
        name='AllCustomer'
    ),

    path(
        'EditCustomer/<id>',
        EditCustomer,
        name='EditCustomer'
    ),

    path(
        'delete/<id>',
        Delete,
        name='delete'
    ),

    path(
        'Search',
        Search,
        name='Search'
    ),

    path(
        'AddCustpage_Delete/<id>',
        AddCustpage_Delete,
        name='AddCustpage_Delete'
    ),

    path(
        'AllCustpage_Delete/<id>',
        AllCustpage_Delete,
        name='AllCustpage_Delete'
    ),

    path(
        'AddEmplopage_Delete/<id>',
        AddEmplopage_Delete,
        name='AddEmplopage_Delete'
    ),

    path(
        'Add_Employee_Search',
        Add_Employee_Search,
        name='Add_Employee_Search'
    ),

    path(
        'AllEmployee_Delete/<id>',
        AllEmployee_Delete,
        name='AllEmployee_Delete'
    ),

    path(
        'Add_room',
        Add_room,
        name='Add_room'
    ),

    path(
        'Add_Room_Search',
        Add_Room_Search,
        name='Add_Room_Search'
    ),

    path(
        'AddRooms_Delete/<id>',
        AddRooms_Delete,
        name='AddRooms_Delete'
    ),

    path(
        'EditRooms/<id>',
        EditRooms,
        name='EditRooms'
    ),

    path(
        'All_Room',
        All_Room,
        name='All_Room'
    ),

    path(
        'AllRooms_Delete/<id>',
        AllRooms_Delete,
        name='AllRooms_Delete'
    ),

    path(
        'AddEmployeeSalary',
        AddEmployeeSalary,
        name='AddEmployeeSalary'
    ),

    path(
        'Salary_Delete/<id>',
        Salary_Delete,
        name='Salary_Delete'
    ),

    path(
        'EmployeeShow',
        EmployeeShow,
        name='EmployeeShow'
    ),
]