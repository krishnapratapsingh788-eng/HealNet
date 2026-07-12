import datetime


def current_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def greeting():

    hour = datetime.datetime.now().hour

    if hour < 12:
        return "Good Morning ☀"

    elif hour < 18:
        return "Good Afternoon 🌤"

    return "Good Evening 🌙"