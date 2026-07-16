"""Извлечение дат
Реализуйте программу, которая должна:
Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Данные:
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."


Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022

"""
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

import re


events_date = re.findall(r"\d{2}[/.-]\d{2}[/.-]\d{4}", text)

for date in events_date:
    print(date)



# 15/03/2025
# 01.12.2024
# 09-09-2023
# 28/02/2022