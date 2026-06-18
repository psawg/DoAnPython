from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from HotelApp import models
from HotelApp.forms import Add_Employee_form, Add_salary_form
from HotelApp.employee_display import DEPARTMENT_CHOICES, GENDER_CHOICES


def _parse_display_count(raw):
    if raw in (None, ''):
        return None
    try:
        count = int(raw)
    except (TypeError, ValueError):
        return None
    return count if count > 0 else None


def _strip_post(request, key):
    return (request.POST.get(key) or '').strip()


def _employee_form_context(**extra):
    context = {
        'department_choices': DEPARTMENT_CHOICES,
        'gender_choices': GENDER_CHOICES,
    }
    context.update(extra)
    return context


def _all_employees_queryset(search=None, limit=None):
    data = models.Add_Employee.objects.all().order_by('-Employee_Id')

    if search:
        data = data.filter(
            Q(Employee_Id__icontains=search)
            | Q(First_Name__icontains=search)
            | Q(Last_Name__icontains=search)
            | Q(Email__icontains=search)
            | Q(Departments__icontains=search)
            | Q(Mobile_Number__icontains=search)
        )

    if limit:
        return data[:limit]

    return data


def Addemployee(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Upload_Image')
        employee_id = _strip_post(request, 'Employee_Id')

        if not employee_id:
            data = models.Add_Employee.objects.all().order_by('-Employee_Id')
            return render(
                request,
                'admin/addemployee.html',
                _employee_form_context(data=data, error='Vui lòng nhập mã nhân viên'),
            )

        if models.Add_Employee.objects.filter(Employee_Id=employee_id).exists():
            data = models.Add_Employee.objects.all().order_by('-Employee_Id')
            return render(
                request,
                'admin/addemployee.html',
                _employee_form_context(data=data, error='Mã nhân viên đã tồn tại'),
            )

        Data = models.Add_Employee()
        Data.Employee_Id = employee_id
        Data.First_Name = _strip_post(request, 'First_Name')
        Data.Last_Name = _strip_post(request, 'Last_Name')
        Data.Email = _strip_post(request, 'Email')
        Data.Mobile_Number = _strip_post(request, 'Mobile_Number')
        Data.Joining_Date = _strip_post(request, 'Joining_Date')
        Data.Dateof_Birth = _strip_post(request, 'Dateof_Birth')
        Data.Departments = _strip_post(request, 'Departments')
        Data.Gender = _strip_post(request, 'Gender')
        Data.Blood_Group = _strip_post(request, 'Blood_Group')
        Data.Education = _strip_post(request, 'Education')
        Data.Personal_Identity = _strip_post(request, 'Personal_Identity')
        Data.Guardian = _strip_post(request, 'Guardian')
        Data.Guardian_Number = _strip_post(request, 'Guardian_Number')
        Data.Upload_Image = upload_image
        Data.Address = _strip_post(request, 'Address')

        try:
            Data.save()
        except Exception:
            data = models.Add_Employee.objects.all().order_by('-Employee_Id')
            return render(
                request,
                'admin/addemployee.html',
                _employee_form_context(
                    data=data,
                    error='Không thể thêm nhân viên. Kiểm tra email, SĐT hoặc CMND đã tồn tại.',
                ),
            )

        return redirect('Addemployee')

    data = models.Add_Employee.objects.all().order_by('-Employee_Id')

    return render(
        request,
        'admin/addemployee.html',
        _employee_form_context(data=data),
    )


def Editemployee(request, id):
    data = models.Add_Employee.objects.get(Employee_Id=id)

    if request.method == 'POST':
        form = Add_Employee_form(
            request.POST,
            request.FILES,
            instance=data,
        )

        if form.is_valid():
            form.save()
            return redirect('Allemployee')

        return HttpResponse('Failed')

    return render(
        request,
        'admin/Editemployee.html',
        {'data': data},
    )


def Allemployee(request):
    display_count = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'all':
            return redirect('Allemployee')

        search = _strip_post(request, 'search')
        display_count = request.POST.get('display_count', '')
        limit = _parse_display_count(display_count)

        data = _all_employees_queryset(search=search, limit=limit)

        return render(
            request,
            'admin/allemployee.html',
            {
                'data': data,
                'display_count': display_count,
                'search': search,
            },
        )

    data = _all_employees_queryset()

    return render(
        request,
        'admin/allemployee.html',
        {'data': data},
    )


def AddEmplopage_Delete(request, id):
    data = models.Add_Employee.objects.get(Employee_Id=id)
    data.delete()
    return redirect('Addemployee')


def Add_Employee_Search(request):
    return redirect('Allemployee')


def AllEmployee_Delete(request, id):
    data = models.Add_Employee.objects.get(Employee_Id=id)
    data.delete()
    return redirect('Allemployee')


def AddEmployeeSalary(request):
    if request.method == 'POST':
        employee_id = _strip_post(request, 'Employee_Id')
        salary = _strip_post(request, 'Salary')

        data = models.Add_Salarys.objects.all().order_by('-id')
        employees = models.Add_Employee.objects.all().order_by('-Employee_Id')

        if not employee_id:
            return render(
                request,
                'admin/AddEmployeeSalary.html',
                _employee_form_context(
                    data=data,
                    employees=employees,
                    error='Vui lòng chọn nhân viên',
                ),
            )

        if not salary:
            return render(
                request,
                'admin/AddEmployeeSalary.html',
                _employee_form_context(
                    data=data,
                    employees=employees,
                    error='Vui lòng nhập mức lương',
                ),
            )

        try:
            employee = models.Add_Employee.objects.get(Employee_Id=employee_id)
        except models.Add_Employee.DoesNotExist:
            return render(
                request,
                'admin/AddEmployeeSalary.html',
                _employee_form_context(
                    data=data,
                    employees=employees,
                    error='Không tìm thấy nhân viên',
                ),
            )

        Data = models.Add_Salarys()
        Data.Employee_Id = employee
        Data.Employee_Name = f'{employee.First_Name} {employee.Last_Name}'.strip()
        Data.Email = employee.Email
        Data.Mobile_Number = str(employee.Mobile_Number)
        Data.Departments = employee.Departments
        Data.Salary = salary
        Data.save()

        return redirect('AddEmployeeSalary')

    data = models.Add_Salarys.objects.all().order_by('-id')
    employees = models.Add_Employee.objects.all().order_by('-Employee_Id')

    return render(
        request,
        'admin/AddEmployeeSalary.html',
        _employee_form_context(data=data, employees=employees),
    )


def Salary_Delete(request, id):
    data = models.Add_Salarys.objects.get(id=id)
    data.delete()
    return redirect('AddEmployeeSalary')
