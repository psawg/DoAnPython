"""Nhãn tiếng Việt cho dữ liệu phòng (hỗ trợ giá trị cũ trong DB)."""

ROOM_TYPE_MAP = {
    'Delux': 'Phòng hạng sang',
    'Super Delux': 'Phòng cao cấp',
    'Single': 'Phòng đơn',
    'Double': 'Phòng đôi',
    'Phòng Hạng Sang': 'Phòng hạng sang',
    'Phòng Cao Cấp': 'Phòng cao cấp',
    'Phòng Đơn': 'Phòng đơn',
    'Phòng Đôi': 'Phòng đôi',
    'Phòng hạng sang': 'Phòng hạng sang',
    'Phòng cao cấp': 'Phòng cao cấp',
    'Phòng đơn': 'Phòng đơn',
    'Phòng đôi': 'Phòng đôi',
}

ROOM_TYPE_CHOICES = [
    'Phòng hạng sang',
    'Phòng cao cấp',
    'Phòng đơn',
    'Phòng đôi',
]

ROOM_FLOOR_MAP = {
    'Floor_G': 'Tầng trệt',
    'Floor_First': 'Tầng 1',
    'Floor_Second': 'Tầng 2',
    'Floor_Thirt': 'Tầng 3',
    'Floor_Third': 'Tầng 3',
    'Room Floor': '',
    'Tầng Trệt': 'Tầng trệt',
    'Tầng trệt': 'Tầng trệt',
    'Tầng 1': 'Tầng 1',
    'Tầng 2': 'Tầng 2',
    'Tầng 3': 'Tầng 3',
}

ROOM_FLOOR_CHOICES = [
    'Tầng trệt',
    'Tầng 1',
    'Tầng 2',
    'Tầng 3',
]


def display_room_type(value):
    if not value:
        return value or ''
    key = str(value).strip()
    return ROOM_TYPE_MAP.get(key, key)


def display_room_floor(value):
    if not value:
        return value or ''
    key = str(value).strip()
    mapped = ROOM_FLOOR_MAP.get(key, key)
    return mapped if mapped else key
