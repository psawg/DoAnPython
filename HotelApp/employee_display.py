"""Nhãn tiếng Việt cho dữ liệu nhân viên."""

DEPARTMENT_CHOICES = [
    'Buồng phòng',
    'Bếp',
    'Quản lý',
    'An ninh',
    'Ẩm thực',
    'Vận tải',
]

GENDER_CHOICES = ['Nam', 'Nữ']

DEPARTMENT_MAP = {
    'Housekeeping': 'Buồng phòng',
    'Kitchen': 'Bếp',
    'Manager': 'Quản lý',
    'Security': 'An ninh',
    'Food and Beverage': 'Ẩm thực',
    'transport': 'Vận tải',
    'Departments': '',
    'Buồng phòng': 'Buồng phòng',
    'Bếp': 'Bếp',
    'Quản lý': 'Quản lý',
    'An ninh': 'An ninh',
    'Ẩm thực': 'Ẩm thực',
    'Vận tải': 'Vận tải',
}

GENDER_MAP = {
    'MALE': 'Nam',
    'FEMALE': 'Nữ',
    'Male': 'Nam',
    'Female': 'Nữ',
    'Nam': 'Nam',
    'Nữ': 'Nữ',
    'Gender': '',
}


def display_department(value):
    if not value:
        return value or ''
    key = str(value).strip()
    return DEPARTMENT_MAP.get(key, key)


def display_gender(value):
    if not value:
        return value or ''
    key = str(value).strip()
    return GENDER_MAP.get(key, key)
