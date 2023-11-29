from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    # Підготовка даних
    birthdays = defaultdict(list)
    today = datetime.today().date()
    week_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # Перебір користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо дата в минулому, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # Визначення дня тижня
        if delta_days < 7:
            day_number = birthday_this_year.weekday()
            day_number = (
                0 if day_number >= 5 else day_number
            )  # Для суботи (5) та неділі (6) переносимо на понеділок (0)

            # Визначення дня тижня
            day = week_days[day_number]
            birthdays[day].append(name)

    # Виведення результату
    if not birthdays:
        print("На наступному тижні дні народження відсутні.")
    else:
        for day in week_days:
            if day in birthdays:
                print(f"{day}: {', '.join(birthdays[day])}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 11, 30)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 6, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 12, 1)},
    {"name": "Jeff Bezos", "birthday": datetime(1964, 12, 1)},
    {"name": "Larry Page", "birthday": datetime(1973, 3, 2)},
    {"name": "Tim Cook", "birthday": datetime(1960, 11, 23)},
]

if __name__ == "__main__":
    get_birthdays_per_week(users)
