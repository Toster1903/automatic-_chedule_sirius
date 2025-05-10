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

data = []
for i in range(amount_of_information):
    day = random.choice(days_of_week)
    group = random.randint(1, 16)
    subject = random.choice(list(subjects.values()))
    name = subject['name']
    difficulty = subject['difficulty']
    temperature = random.randint(-5, 35)
    precipitation = bool(random.randint(0, 1))
    type_prec = random.choice(['солнечно', 'пасмурно', 'ветер', 'туман'])
    num_classes = random.randint(1, 5)
    class_numbers = sorted(random.sample(range(1, 9), num_classes))
    performance = random.randint(50, 100)
    attendance = random.randint(50, 100)

    record = {
        'день': day,
        'группа': group,
        'предмет': name,
        'сложность': difficulty,
        'температура': temperature,
        'осадки': precipitation,
        'тип погоды': type_prec,
        'количество пар': num_classes,
        'номера пар': class_numbers,
        'успеваемость': performance,
        'процент посещаемости': attendance
    }
    data.append(record)


