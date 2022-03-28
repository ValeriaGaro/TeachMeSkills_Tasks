# Сделать свой декоратор
def decorate_func(func):

    def wrapper(num):
        print("Сейчас я выведу список нечетных чисел")
        print(func(num))
        print("На этом все")
    return wrapper


@decorate_func
def odd_numbers(number: int) -> list:
    """Данная функция выводит список нечетных чисел в введенном пользователе диапазоне"""
    users_numbers = [number for number in range(number) if number % 2 != 0]
    return users_numbers


odd_numbers(10)

# Сделать лямбда-функцию
"""Данная лямба функция принимает два числа и возвращает остаток от деления первого числа на другое"""
reminder_of_division = lambda x, y: x % y
print(reminder_of_division(3, 2))