from datetime import datetime
import time

# Создать генератор для заполнения списка
user_list = [i for i in range(1, 51) if i % 5 == 0]
print(user_list)

# Создать функцию для генерации списков с аннотациями


def generate_list(end_number: int ) -> list:
    gen_list = [i for i in range(0, end_number + 1)]
    return gen_list


print(generate_list(10))
print(generate_list(20))


# Создать функцию, которая будет вызываться из генератора и отдавать текущее время


def return_time(number_iterations: int = 1):
    list_times = []
    for i in range(1, number_iterations + 1):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        list_times.append(current_time)
        time.sleep(2)
    return list_times


current_times_list = [i for i in return_time(5)]
print(current_times_list)


