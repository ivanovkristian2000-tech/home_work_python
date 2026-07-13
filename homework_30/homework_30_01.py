"""01 Анализ курсов студентов

Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
    - Имя
    - дату рождения (birth_date) в формате дд.мм.гггг
    - дату поступления (enrollment_date) в том же формате
    - список курсов.

2. Вычислить:
    - общее количество студентов.
    - средний возраст на момент поступления.
    - количество студентов на каждом курсе.

3. Сохранить отчёт в JSON-файл student_courses_report.json.
"""
import datetime
import json
from collections import Counter
from datetime import datetime
from dateutil.relativedelta import relativedelta


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
       return json.load(f)




def get_info():
    info = read_json("student_courses.json")
    """
    "name": "Diana Williams",
    "birth_date": "12.06.1983",
    "enrollment_date": "29.04.2023",
    "courses": [
      "Physics",
      "Chemistry"
    ]
    """
    count_of_students = len(info)
    courses_counter = Counter()
    total_age = 0

    for student in info:
        for course in student["courses"]:
            courses_counter[course] += 1

        birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")
        enrollment_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")
        age = relativedelta(enrollment_date, birth_date).years

        total_age += age

    courses_counter = dict(courses_counter)
    average_age = total_age / count_of_students


    report = {
        "total_students": count_of_students,
        "average_age_of_students": average_age,
        "courses_count": courses_counter
    }

    print("Отчет успешно сохранен в student_courses_report.json")
    print(json.dumps(report, indent=4, ensure_ascii=False))

    return report




def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as w:
        json.dump(data, w, indent=4, ensure_ascii=False)





report = get_info()
write_json("student_courses_report.json", report)