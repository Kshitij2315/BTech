for hour in range(24):
    if hour == 0:
        print("12 Midnight")
    elif hour < 12:
        print(hour, "AM")
    elif hour == 12:
        print("12 Noon")
    else:
        print(hour - 12, "PM")