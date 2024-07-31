### Задание 1

total_seconds = int(input("Введите количество секунд: "))
def format_seconds(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    formatted_time = f"{days} days {hours} hours {minutes} minutes {seconds} seconds"
    return formatted_time

# Пример использования:
formatted_result = format_seconds(total_seconds)
print(f"Форматированное время: {formatted_result}")  # Выведет: '1 days 10 hours 17 minutes 36 seconds'

### Задание 2

user_numbers = input("Введите числа от 1 до 10 через запятую: ")
numbers = user_numbers.split(',')
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
print("Чётные числа: ", even_numbers)