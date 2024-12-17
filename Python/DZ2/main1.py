def format_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{days}:{hours}:{minutes}:{seconds}"

seconds = 10000
formatted_time = format_seconds(seconds)
print(formatted_time)
