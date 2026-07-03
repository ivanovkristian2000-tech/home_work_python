"""План по дням недели

Напишите программу, которая помогает планировать дела.
Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.

Данные:
"""
# Расписание дел на неделю

weekly_schedule = {

    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Rest"],

    "Sunday": ["Family time", "Rest"]

}

""" 
Пример ввода:

Нажмите 'Enter' для получения плана: 

Monday: Gym, Work, Read book

Нажмите 'Enter' для получения плана: 

Tuesday: Meeting, Work, Study Python

...

Нажмите 'Enter' для получения плана: 

Sunday: Family time, Rest

Нажмите 'Enter' для получения плана: 

Monday: Gym, Work, Read book

Нажмите 'Enter' для получения плана: q

...
"""
import itertools


def plan(next_day: dict) -> None:

    key_value = next_day.items()
    days = itertools.cycle(key_value)

    while True:

        user = input("Нажмите 'Enter' для получения плана или нажмите 'q' для выхода: ")

        if not user:
            current_day = next(days)
            day = current_day[0]
            tasks = ", ".join(current_day[1])
            print(f"{day}: {tasks}")

        elif user == 'q':
            break
        else:
            print("Не корректный ввод")





plan(weekly_schedule)
