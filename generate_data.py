import random

days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

amount_of_information = 40

subjects = {
    1: {"name": "Русский язык", "difficulty": 3},
    2: {"name": "Литература", "difficulty": 3},
    3: {"name": "Математика", "difficulty": 5},
    4: {"name": "Геометрия", "difficulty": 4},
    5: {"name": "Естествознание", "difficulty": 3},
    6: {"name": "Информатика", "difficulty": 5},
    7: {"name": "Физика", "difficulty": 4},
    8: {"name": "История", "difficulty": 2},
    9: {"name": "Обществознание", "difficulty": 2},
    10: {"name": "Основы информационных технологий", "difficulty": 4},
    11: {"name": "Основы программирования", "difficulty": 5},
    12: {"name": "Математические основы информатики", "difficulty": 4},
    13: {"name": "Основы сетевых технологий", "difficulty": 4},
    14: {"name": "Операционные системы", "difficulty": 4},
    15: {"name": "Базы данных", "difficulty": 4},
    16: {"name": "Прикладное программирование", "difficulty": 5},
    17: {"name": "Системное администрирование", "difficulty": 4},
    18: {"name": "Информационная безопасность", "difficulty": 5},
    19: {"name": "Архитектура компьютеров", "difficulty": 4},
    20: {"name": "Техническое обслуживание компьютерных систем", "difficulty": 3},
    21: {"name": "Эксплуатация компьютерных сетей", "difficulty": 4},
    22: {"name": "Диагностика и ремонт оборудования", "difficulty": 4},
    23: {"name": "Сетевые операционные системы", "difficulty": 4},
    24: {"name": "Конфигурирование и администрирование сетей", "difficulty": 5},
    25: {"name": "Безопасность сетей", "difficulty": 5},
    26: {"name": "Виртуализация и облачные технологии", "difficulty": 4},
    27: {"name": "Разработка программного обеспечения", "difficulty": 5},
    28: {"name": "Проектирование информационных систем", "difficulty": 4},
    29: {"name": "Тестирование программных продуктов", "difficulty": 4},
    30: {"name": "Веб-технологии", "difficulty": 4},
    31: {"name": "Методы и средства защиты информации", "difficulty": 5},
    32: {"name": "Криптография", "difficulty": 5},
    33: {"name": "Безопасность операционных систем и сетей", "difficulty": 5},
    34: {"name": "Администрирование систем защиты", "difficulty": 5},
    35: {"name": "Основы туризма и гостеприимства", "difficulty": 3},
    36: {"name": "Организация обслуживания в гостиницах", "difficulty": 3},
    37: {"name": "Маркетинг и менеджмент в сфере услуг", "difficulty": 3},
    38: {"name": "Проектно-исследовательская деятельность", "difficulty": 4}
}




def adjust_attendance(base_attendance, precipitation, difficulty, temperature, day):

    if precipitation:
        base_attendance -= random.randint(15, 25)


    if difficulty >= 4:
        base_attendance -= random.randint(5, 10)


    if temperature > 30 or temperature < -5:
        base_attendance -= random.randint(10, 15)


    if day == 'Суббота':
        base_attendance -= random.randint(5, 10)

    return max(30, min(100, base_attendance))


def adjust_performance(base_performance, attendance, difficulty):
    performance = base_performance * (attendance / 100)
    if difficulty >= 4:
        performance -= random.randint(5, 15)
    return max(20, min(100, int(performance)))


data = []
for i in range(amount_of_information):
    day = random.choice(days_of_week)
    group = random.randint(1, 16)
    subject = random.choice(list(subjects.values()))


    base_attendance = random.randint(70, 90) if subject['difficulty'] < 4 else random.randint(50, 80)
    base_performance = random.randint(60, 90) if subject['difficulty'] < 4 else random.randint(50, 75)


    temperature = random.randint(-5, 35)
    if random.random() < 0.3:
        precipitation = True
        type_prec = random.choice(['дождь', 'снег', 'град'])
    else:
        precipitation = False
        type_prec = random.choice(['солнечно', 'пасмурно', 'ветер', 'туман'])
    num_classes = random.randint(1, 3) if day == 'Суббота' else random.randint(2, 5)
    class_numbers = sorted(random.sample(range(1, 9), num_classes))
    if num_classes == 1:  # Для единообразия вывода
        class_numbers = [class_numbers[0]]


    attendance = adjust_attendance(base_attendance, precipitation, subject['difficulty'], temperature, day)
    performance = adjust_performance(base_performance, attendance, subject['difficulty'])

    record = {
        'день': day,
        'группа': group,
        'предмет': subject['name'],
        'сложность': subject['difficulty'],
        'температура': temperature,
        'осадки': precipitation,
        'тип погоды': type_prec,
        'количество пар': num_classes,
        'номера пар': class_numbers,
        'успеваемость': performance,
        'процент посещаемости': attendance
    }
    data.append(record)


for entry in data[:3]:
    print(entry)
