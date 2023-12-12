def determine_season(month, day):
    seasons = {
        "Spring": (3, 20),
        "Summer": (6, 21),
        "Fall": (9, 22),
        "Winter": (12, 21)
    }

    month = month.lower()
    for season, start_date in seasons.items():
        if (month, day) >= start_date:
            current_season = season
    return current_season
input_month = input("Enter the month (e.g., Jan, Feb, Mar): ")
input_day = int(input("Enter the day: "))
result = determine_season(input_month, input_day)
print(f"The season is {result}.")
